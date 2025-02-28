class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get_sequence_data(self, sequence_id):
        response = requests.get(f"{self.base_url}/sequences/{sequence_id}", headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def upload_sequence_data(self, sequence_data):
        response = requests.post(f"{self.base_url}/sequences", json=sequence_data, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }