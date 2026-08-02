import unittest
from unittest.mock import patch

from fastapi import FastAPI
from fastapi.testclient import TestClient

from routers.sql import router


class SqlRouterTests(unittest.TestCase):
    def setUp(self):
        app = FastAPI()
        app.include_router(router)
        self.client = TestClient(app)

    @patch("routers.sql.ask_database")
    def test_execute_accepts_json_body_question(self, ask_database_mock):
        ask_database_mock.return_value = {
            "question": "List customers",
            "generated_sql": "SELECT * FROM customers",
            "columns": ["id"],
            "rows": [[1]],
            "row_count": 1,
            "execution_time_ms": 10,
        }

        response = self.client.post(
            "/execute",
            json={"question": "List customers"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["question"], "List customers")


if __name__ == "__main__":
    unittest.main()
