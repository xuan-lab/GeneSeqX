class SequenceViewer:
    def __init__(self, sequence_data):
        self.sequence_data = sequence_data

    def display_sequence(self):
        # Code to display the gene sequence in a user-friendly format
        print("Displaying sequence:")
        print(self.sequence_data)

    def visualize_features(self, features):
        # Code to visualize specific features of the gene sequence
        print("Visualizing features:")
        for feature in features:
            print(f"Feature: {feature}")

    def plot_sequence(self):
        # Code to generate plots for the gene sequence
        print("Generating sequence plot...")