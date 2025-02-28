def plot_sequence_distribution(sequences):
    import matplotlib.pyplot as plt
    import numpy as np

    lengths = [len(seq) for seq in sequences]
    plt.hist(lengths, bins=30, alpha=0.7, color='blue')
    plt.title('Distribution of Sequence Lengths')
    plt.xlabel('Length')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def plot_gc_content(sequences):
    import matplotlib.pyplot as plt

    gc_content = [(seq.count('G') + seq.count('C')) / len(seq) * 100 for seq in sequences]
    plt.plot(gc_content, marker='o', linestyle='-', color='green')
    plt.title('GC Content of Sequences')
    plt.xlabel('Sequence Index')
    plt.ylabel('GC Content (%)')
    plt.grid(True)
    plt.show()

def plot_sequence_similarity(similarity_matrix):
    import seaborn as sns
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 8))
    sns.heatmap(similarity_matrix, cmap='viridis', annot=True)
    plt.title('Sequence Similarity Matrix')
    plt.xlabel('Sequence Index')
    plt.ylabel('Sequence Index')
    plt.show()