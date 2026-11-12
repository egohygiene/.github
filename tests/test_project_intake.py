"""Synthetic read-only transport regressions; no provider calls or credentials."""
import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location("preview_project_intake", Path(__file__).resolve().parents[1] / "scripts/preview_project_intake.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


def project(items=(), more=False, cursor=None):
    return {"data": {"organization": {"projectV2": {"id": "PVT_synthetic", "number": 1,
        "title": "Synthetic", "url": "https://github.com/orgs/egohygiene/projects/1", "closed": False,
        "items": {"nodes": list(items), "pageInfo": {"hasNextPage": more, "endCursor": cursor}}}}}}


def issue(number):
    return {"number": number, "state": "open", "node_id": f"I_synthetic{number}",
        "html_url": f"https://github.com/egohygiene/example/issues/{number}"}


def item(number, identity):
    return {"id": identity, "isArchived": False, "content": {"__typename": "Issue", "id": f"I_synthetic{number}",
        "number": number, "url": issue(number)["html_url"],
        "repository": {"nameWithOwner": "egohygiene/example", "visibility": "PUBLIC"}}}


class Fake:
    def __init__(self, responses):
        self.responses = iter(responses)
        self.requests = []

    def request(self, endpoint, payload=None):
        self.requests.append((endpoint, payload))
        response = next(self.responses)
        if isinstance(response, Exception):
            raise response
        return response


class PreviewCases(unittest.TestCase):
    def test_membership_is_read_only_and_private_content_is_not_counted(self):
        hidden = {"id": "private", "content": {"__typename": "Issue", "repository": {"visibility": "PRIVATE"}}}
        client = Fake([project([item(1, "one"), item(2, "two"), item(2, "duplicate"), hidden]),
            [{"id": 1, "full_name": "egohygiene/example", "private": False, "visibility": "public"}],
            [issue(1), issue(2), issue(3), {"pull_request": {}}]])
        result = module.preview(client)
        self.assertTrue(result["complete"])
        self.assertEqual([row["membership"] for row in result["repositories"][0]["issues"]], ["existing", "duplicate", "missing"])
        self.assertEqual(result["writes"], 0)
        self.assertNotIn("private", str(result))
        self.assertEqual(client.requests[0][1]["query"], module.QUERY)

    def test_project_pagination_continues_and_repeated_cursor_fails(self):
        client = Fake([project(more=True, cursor="next"), project(more=True, cursor="next")])
        result = module.preview(client)
        self.assertFalse(result["complete"])
        self.assertEqual(result["errors"], ["PROJECT_CURSOR_INVALID"])
        self.assertEqual(client.requests[1][1]["variables"]["cursor"], "next")

    def test_partial_repository_failure_never_becomes_existing(self):
        client = Fake([project(), [{"id": 1, "full_name": "egohygiene/example", "private": False, "visibility": "public"}],
            module.IntakeError("PROVIDER_ACCESS_RATE_OR_TRANSPORT_FAILURE")])
        result = module.preview(client)
        self.assertFalse(result["complete"])
        self.assertEqual(result["repositories"][0]["state"], "incomplete")
        self.assertEqual(result["summary"]["existing"], 0)

    def test_full_rest_page_at_budget_is_incomplete(self):
        client = Fake([list(range(100))])
        with self.assertRaisesRegex(module.IntakeError, "REST_PAGINATION_LIMIT"):
            list(module.pages(client, "/synthetic", 1))

    def test_graphql_error_never_produces_membership_decisions(self):
        result = module.preview(Fake([{"errors": [{"message": "synthetic denial"}]}]))
        self.assertFalse(result["complete"])
        self.assertEqual(result["repositories"], [])


if __name__ == "__main__":
    unittest.main()
