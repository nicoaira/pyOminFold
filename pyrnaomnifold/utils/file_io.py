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

def bpseq_to_dot_bracket(bpseq_content):
    """
    Converts BPSEQ format content to dot-bracket notation.

    Args:
        bpseq_content (str): BPSEQ content as a string.

    Returns:
        str: RNA secondary structure in dot-bracket notation.
    """
    lines = bpseq_content.strip().split('\n')
    sequence_length = len(lines)
    paired_indices = [0] * sequence_length

    for line in lines:
        parts = line.split()
        if len(parts) >= 3:
            idx = int(parts[0]) - 1  # BPSEQ indices start at 1
            paired_idx = int(parts[2]) - 1
            paired_indices[idx] = paired_idx

    # Generate dot-bracket notation
    structure = ['.'] * sequence_length
    stack = []

    for i in range(sequence_length):
        if paired_indices[i] > i:
            structure[i] = '('
            stack.append(i)
        elif paired_indices[i] < i:
            if stack:
                open_idx = stack.pop()
                structure[open_idx] = '('
                structure[i] = ')'

    return ''.join(structure)
