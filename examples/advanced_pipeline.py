from src.core.data_manager import DataManager
from src.core.sequence import Sequence
from src.analysis.alignment import Alignment
from src.analysis.phylogeny import Phylogeny
from src.analysis.statistics import Statistics
from src.visualization.sequence_viewer import SequenceViewer
from src.pipelines.workflow import Workflow

def main():
    # Initialize the DataManager
    data_manager = DataManager()

    # Load gene sequence data
    sequences = data_manager.load_sequences("data/sequences.fasta")

    # Perform sequence alignment
    alignment = Alignment()
    aligned_sequences = alignment.perform_alignment(sequences)

    # Conduct statistical analysis
    stats = Statistics()
    snp_count = stats.calculate_snps(aligned_sequences)

    # Construct phylogenetic tree
    phylogeny = Phylogeny()
    tree = phylogeny.construct_tree(aligned_sequences)

    # Visualize the results
    viewer = SequenceViewer()
    viewer.display_sequences(aligned_sequences)
    viewer.plot_phylogenetic_tree(tree)

    # Execute the workflow
    workflow = Workflow()
    workflow.run_pipeline(sequences)

if __name__ == "__main__":
    main()