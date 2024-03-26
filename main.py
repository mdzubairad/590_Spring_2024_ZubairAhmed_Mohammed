import pandas as pd
from Bio import SeqIO

# Define your functions before using them
def load_genomic_data(filepath):
    sequences = []
    for seq_record in SeqIO.parse(filepath, "fasta"):
        sequences.append(str(seq_record.seq))
    return sequences

def load_epi_data(filepath):
    epi_data = pd.read_csv(filepath)
    return epi_data

# Correct the paths
genomic_data_path = r'C:\Users\Zubair\OneDrive\Documents\CSUDH\Sem 4\CSC 590\Project\Geonomics\sequences.fasta'
epidemiological_data_path = r'C:\Users\Zubair\OneDrive\Documents\CSUDH\Sem 4\CSC 590\Project\epidemiological\cases.csv'

# Now, you can use these paths to load your data
genomic_sequences = load_genomic_data(genomic_data_path)
epi_data = load_epi_data(epidemiological_data_path)

# Example of one-hot encoding genomic sequences (simplified)
def one_hot_encode_sequences(sequences):
    # This is a simplified example. You'll need a more comprehensive approach
    # to handle the full complexity of genomic sequences.
    mapping = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1]}
    encoded_sequences = [[mapping[nuc] for nuc in seq] for seq in sequences]
    return encoded_sequences
