
import unittest
from app import health_check


class TestHealthCheck(unittest.TestCase):
    def test_application_is_healthy(self):
        result = health_check()

        self.assertEqual(
            result["application"],
            "talent-acquisition"
        )
        self.assertEqual(result["status"], "healthy")


if __name__ == "__main__":
    unittest.main()
