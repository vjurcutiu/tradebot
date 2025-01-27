import unittest
import requests

class TestBlockNumberEndpoint(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000"  # Update this if your Flask app is running on a different URL

    def test_get_block_number_success(self):    
        """Test that the /api/block-number endpoint returns a valid block number."""
        response = requests.get(f"{self.BASE_URL}/api/block-number")
        print(response.json())  # Debugging: Print the response
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("block_number", data)
        self.assertIsInstance(data["block_number"], int)
        self.assertGreater(data["block_number"], 0)  # Block number should be greater than 0 # Block number should be greater than 0

    def test_get_block_number_error_handling(self):
        """Test that the /api/block-number endpoint handles errors gracefully."""
        # Simulate an error by passing the `force_error=true` query parameter
        response = requests.get(f"{self.BASE_URL}/api/block-number?force_error=true")
        self.assertEqual(response.status_code, 500)
        self.assertIn("error", response.json())

if __name__ == "__main__":
    unittest.main()