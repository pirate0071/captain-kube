import unittest
from unittest.mock import patch, MagicMock
from modules.find_unused_resources import detect_unused_resources

class TestFindUnusedResources(unittest.TestCase):
    
    @patch("modules.find_unused_resources.client.CoreV1Api")
    def test_detect_unused_resources(self, mock_k8s_client):
        mock_api = MagicMock()
        mock_k8s_client.return_value = mock_api
        
        # Mock PVCs
        mock_pvc = MagicMock()
        mock_pvc.metadata.name = "unused-pvc"
        mock_pvc.spec.volume_name = "vol-1"
        
        # Mock Persistent Volumes
        mock_pv = MagicMock()
        mock_pv.spec.volume_name = "vol-2"

        mock_api.list_persistent_volume_claim_for_all_namespaces.return_value.items = [mock_pvc]
        mock_api.list_persistent_volume_for_all_namespaces.return_value.items = [mock_pv]
        
        detect_unused_resources()

if __name__ == "__main__":
    unittest.main()