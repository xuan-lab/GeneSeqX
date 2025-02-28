from scipy import stats
import numpy as np

class Statistics:
    @staticmethod
    def calculate_snp(sequence1, sequence2):
        """Calculate the number of SNPs between two sequences."""
        if len(sequence1) != len(sequence2):
            raise ValueError("Sequences must be of the same length.")
        snp_count = sum(1 for a, b in zip(sequence1, sequence2) if a != b)
        return snp_count

    @staticmethod
    def calculate_indels(sequence1, sequence2):
        """Calculate the number of INDELs between two sequences."""
        # This is a simple implementation; a more complex algorithm may be needed for real applications.
        len_diff = abs(len(sequence1) - len(sequence2))
        return len_diff

    @staticmethod
    def calculate_gc_content(sequence):
        """Calculate the GC content of a sequence."""
        g_count = sequence.count('G')
        c_count = sequence.count('C')
        return (g_count + c_count) / len(sequence) * 100 if len(sequence) > 0 else 0

    @staticmethod
    def perform_statistical_test(data1, data2):
        """Perform a t-test on two sets of data."""
        t_stat, p_value = stats.ttest_ind(data1, data2)
        return t_stat, p_value

    @staticmethod
    def summarize_sequence(sequence):
        """Provide a summary of the sequence."""
        length = len(sequence)
        gc_content = Statistics.calculate_gc_content(sequence)
        snp_count = Statistics.calculate_snp(sequence, sequence)  # Placeholder for comparison
        return {
            "length": length,
            "gc_content": gc_content,
            "snp_count": snp_count
        }