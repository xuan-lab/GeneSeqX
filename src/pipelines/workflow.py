class Workflow:
    def __init__(self, data_manager, analysis_module, visualization_module):
        self.data_manager = data_manager
        self.analysis_module = analysis_module
        self.visualization_module = visualization_module

    def run_analysis(self, sequence_file):
        sequences = self.data_manager.load_sequences(sequence_file)
        alignment_results = self.analysis_module.align_sequences(sequences)
        statistics = self.analysis_module.calculate_statistics(sequences)
        return alignment_results, statistics

    def visualize_results(self, alignment_results, statistics):
        self.visualization_module.plot_alignment(alignment_results)
        self.visualization_module.plot_statistics(statistics)

    def execute_pipeline(self, sequence_file):
        alignment_results, statistics = self.run_analysis(sequence_file)
        self.visualize_results(alignment_results, statistics)