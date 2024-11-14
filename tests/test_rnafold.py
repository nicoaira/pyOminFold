# tests/test_rnafold.py
import pytest
from pyrnaomnifold.methods.rnafold.rnafold_wrapper import RNAfoldWrapper
from pyrnaomnifold.utils.file_io import read_fasta_sequences

def test_rnafold_wrapper():
    # Initialize RNAfold wrapper
    wrapper = RNAfoldWrapper()

    # Load test sequences from the FASTA file
    sequences = read_fasta_sequences("tests/test_sequences.fasta")

    # Test RNAfold on each sequence
    for sequence in sequences:
        structure = wrapper.fold(sequence)
        assert isinstance(structure, str)  # Ensure the structure is a string
        assert len(structure) == len(sequence)  # The structure length should match sequence length
