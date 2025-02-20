import unittest
from unittest.mock import patch, MagicMock
from modules.privilege_detector import check_pod_privileges

class TestPrivilegeDetector(unittest.TestCase):

    @patch("modules.privilege_detector.client.CoreV1Api")
    def test_detect_pod_privileges(self, mock_k8s_client):
        mock_api = MagicMock()
        mock_k8s_client.return_value = mock_api

        mock_pod = MagicMock()
        mock_pod.metadata.name = "privileged-pod"
        mock_pod.metadata.namespace = "default"
        mock_container = MagicMock()
        mock_container.security_context = MagicMock(privileged=True)

        mock_pod.spec.containers = [mock_container]
        mock_api.list_pod_for_all_namespaces.return_value.items = [mock_pod]

        check_pod_privileges()

if __name__ == "__main__":
    unittest.main()