from Bio import SeqIO

def read_fasta_sequences(filepath):
    """
    Reads RNA sequences from a FASTA file.

    Args:
        filepath (str): Path to the FASTA file.

    Returns:
        list: A list of RNA sequences as strings.
    """
    sequences = []
    with open(filepath, "r") as fasta_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
            sequences.append(str(record.seq))
    return sequences
