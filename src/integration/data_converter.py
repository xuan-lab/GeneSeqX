def convert_fasta_to_dict(fasta_file):
    sequences = {}
    with open(fasta_file, 'r') as file:
        sequence_id = None
        sequence_data = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence_id:
                    sequences[sequence_id] = ''.join(sequence_data)
                sequence_id = line[1:]  # Remove '>'
                sequence_data = []
            else:
                sequence_data.append(line)
        if sequence_id:
            sequences[sequence_id] = ''.join(sequence_data)
    return sequences

def convert_dict_to_fasta(sequences, output_file):
    with open(output_file, 'w') as file:
        for seq_id, seq in sequences.items():
            file.write(f'>{seq_id}\n')
            for i in range(0, len(seq), 60):
                file.write(f'{seq[i:i+60]}\n')

def convert_fastq_to_dict(fastq_file):
    sequences = {}
    with open(fastq_file, 'r') as file:
        while True:
            header = file.readline().strip()
            if not header:
                break
            sequence = file.readline().strip()
            plus = file.readline().strip()
            quality = file.readline().strip()
            sequence_id = header[1:]  # Remove '@'
            sequences[sequence_id] = sequence
    return sequences

def convert_dict_to_fastq(sequences, output_file, quality='I'):
    with open(output_file, 'w') as file:
        for seq_id, seq in sequences.items():
            file.write(f'@{seq_id}\n')
            file.write(f'{seq}\n')
            file.write(f'+\n')
            file.write(f'{"".join([quality] * len(seq))}\n')  # Dummy quality scores

def convert_bam_to_dict(bam_file):
    import pysam
    sequences = {}
    with pysam.AlignmentFile(bam_file, "rb") as bam:
        for read in bam:
            sequences[read.query_name] = read.query_sequence
    return sequences

def convert_dict_to_bam(sequences, output_file):
    import pysam
    with pysam.AlignmentFile(output_file, "wb", header={'HD': {'VN': '1.0', 'SO': 'unsorted'}}) as bam:
        for seq_id, seq in sequences.items():
            bam.write(pysam.AlignedSegment(bam.header, query_name=seq_id, query_sequence=seq))

def convert_vcf_to_dict(vcf_file):
    variants = {}
    with open(vcf_file, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            variants[parts[2]] = {
                'chrom': parts[0],
                'pos': parts[1],
                'id': parts[2],
                'ref': parts[3],
                'alt': parts[4],
                'qual': parts[5],
                'filter': parts[6],
                'info': parts[7],
            }
    return variants

def convert_dict_to_vcf(variants, output_file):
    with open(output_file, 'w') as file:
        file.write('##fileformat=VCFv4.2\n')
        file.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n')
        for var_id, var in variants.items():
            file.write(f"{var['chrom']}\t{var['pos']}\t{var['id']}\t{var['ref']}\t{var['alt']}\t{var['qual']}\t{var['filter']}\t{var['info']}\n")