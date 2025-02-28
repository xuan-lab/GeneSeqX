import unittest
from src.core.data_manager import DataManager
from src.core.config import Config

class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.data_manager = DataManager()
        self.config = Config()

    def test_read_fasta(self):
        # Assuming a method read_fasta exists in DataManager
        sequences = self.data_manager.read_fasta('test_sequences.fasta')
        self.assertIsInstance(sequences, list)
        self.assertGreater(len(sequences), 0)

    def test_write_fasta(self):
        # Assuming a method write_fasta exists in DataManager
        result = self.data_manager.write_fasta('output.fasta', ['ATGC', 'CGTA'])
        self.assertTrue(result)

    def test_load_config(self):
        # Assuming a method load exists in Config
        config_data = self.config.load('config.yaml')
        self.assertIn('some_setting', config_data)

if __name__ == '__main__':
    unittest.main()