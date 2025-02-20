import unittest
from unittest.mock import patch
from modules.helm_validator import validate_helm

class TestHelmValidator(unittest.TestCase):

    @patch("modules.helm_validator.subprocess.run")
    def test_validate_helm_chart_success(self, mock_subprocess):
        mock_subprocess.return_value.returncode = 0
        validate_helm("test_chart")

    @patch("modules.helm_validator.subprocess.run")
    def test_validate_helm_chart_failure(self, mock_subprocess):
        mock_subprocess.return_value.returncode = 1
        validate_helm("invalid_chart")

if __name__ == "__main__":
    unittest.main()