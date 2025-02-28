import unittest
from src.analysis.alignment import Alignment
from src.analysis.statistics import Statistics

class TestAnalysis(unittest.TestCase):

    def setUp(self):
        self.alignment = Alignment()
        self.statistics = Statistics()

    def test_sequence_alignment(self):
        seq1 = "ACGT"
        seq2 = "ACG"
        result = self.alignment.align(seq1, seq2)
        self.assertIsNotNone(result)
        self.assertEqual(result['score'], 3)  # Example expected score

    def test_snp_calculation(self):
        reference = "ACGT"
        variant = "ACCT"
        snps = self.statistics.calculate_snps(reference, variant)
        self.assertEqual(snps, 1)  # Example expected SNP count

    def test_indel_calculation(self):
        reference = "ACGT"
        variant = "A--GT"
        indels = self.statistics.calculate_indels(reference, variant)
        self.assertEqual(indels, 2)  # Example expected INDEL count

if __name__ == '__main__':
    unittest.main()