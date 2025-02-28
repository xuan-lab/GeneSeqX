# FILE: /GeneSeqX/GeneSeqX/examples/basic_usage.py
from src.core.data_manager import DataManager
from src.core.sequence import Sequence
from src.analysis.alignment import Alignment
from src.visualization.sequence_viewer import SequenceViewer

def main():
    # Initialize the data manager
    data_manager = DataManager()

    # Load a gene sequence from a FASTA file
    sequence = data_manager.load_sequence("path/to/sequence.fasta")

    # Perform some basic analysis
    alignment = Alignment()
    aligned_sequence = alignment.perform_alignment(sequence)

    # Visualize the aligned sequence
    viewer = SequenceViewer()
    viewer.display_sequence(aligned_sequence)

if __name__ == "__main__":
    main()