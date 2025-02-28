class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence.upper()

    def get_length(self):
        return len(self.sequence)

    def complement(self):
        complement_map = str.maketrans('ATCG', 'TAGC')
        return self.sequence.translate(complement_map)

    def reverse_complement(self):
        return self.complement()[::-1]

    def gc_content(self):
        g_count = self.sequence.count('G')
        c_count = self.sequence.count('C')
        return (g_count + c_count) / self.get_length() * 100

    def transcribe(self):
        return self.sequence.replace('T', 'U')

    def translate(self):
        codon_table = {
            'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
            'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine',
            'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
            'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan', 'UAA': 'Stop',
            'UAG': 'Stop', 'UGA': 'Stop'
        }
        protein = []
        for i in range(0, len(self.sequence), 3):
            codon = self.sequence[i:i+3]
            if codon in codon_table:
                protein.append(codon_table[codon])
            else:
                protein.append('Unknown')
        return protein

    def __str__(self):
        return self.sequence