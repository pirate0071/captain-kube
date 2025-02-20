import unittest
from unittest.mock import patch, MagicMock
from modules.security_scanner import scan_k8s_security

class TestSecurityScanner(unittest.TestCase):

    @patch("modules.security_scanner.client.RbacAuthorizationV1Api")
    def test_scan_k8s_security(self, mock_k8s_client):
        mock_api = MagicMock()
        mock_k8s_client.return_value = mock_api

        mock_role = MagicMock()
        mock_role.metadata.namespace = "default"
        mock_role.metadata.name = "admin-role"

        # Properly mock role rules as objects with attributes
        mock_rule = MagicMock()
        mock_rule.resources = ["*"]
        mock_rule.verbs = ["*"]
        mock_role.rules = [mock_rule]  # Assign as a list of MagicMock objects

        mock_api.list_role_for_all_namespaces.return_value.items = [mock_role]

        # Run the function and ensure it does not raise an error
        scan_k8s_security()

if __name__ == "__main__":
    unittest.main()
