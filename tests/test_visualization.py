import unittest
from src.visualization.sequence_viewer import SequenceViewer

class TestSequenceViewer(unittest.TestCase):

    def setUp(self):
        self.viewer = SequenceViewer()

    def test_visualization_initialization(self):
        self.assertIsNotNone(self.viewer)

    def test_display_sequence(self):
        sequence = "ATCG"
        result = self.viewer.display_sequence(sequence)
        self.assertIn("ATCG", result)

    def test_plot_sequence_distribution(self):
        sequence = "ATCGATCG"
        result = self.viewer.plot_sequence_distribution(sequence)
        self.assertTrue(result)  # Assuming the plot function returns True on success

    def test_handle_empty_sequence(self):
        sequence = ""
        result = self.viewer.display_sequence(sequence)
        self.assertEqual(result, "No sequence to display.")

if __name__ == '__main__':
    unittest.main()