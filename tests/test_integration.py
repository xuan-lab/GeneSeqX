import unittest
from src.integration.api_client import APIClient
from src.integration.data_converter import convert_data_format

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.api_client = APIClient()
        self.test_data = {
            'sequence': 'ATCG',
            'format': 'FASTA'
        }

    def test_api_connection(self):
        response = self.api_client.connect()
        self.assertTrue(response['status'], "API connection failed")

    def test_data_conversion(self):
        converted_data = convert_data_format(self.test_data, 'FASTA', 'FASTQ')
        self.assertIn('converted_sequence', converted_data)
        self.assertEqual(converted_data['format'], 'FASTQ')

if __name__ == '__main__':
    unittest.main()