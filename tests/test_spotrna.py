# tests/test_spotrna.py
import pytest
from pyrnaomnifold.methods.spotrna.spotrna_wrapper import SPOTRNAWrapper
from pyrnaomnifold.utils.file_io import read_fasta_sequences

def test_spotrna_wrapper():
    # Initialize SPOT-RNA wrapper
    wrapper = SPOTRNAWrapper()

    # Load test sequences from the FASTA file
    sequences = read_fasta_sequences("tests/test_sequences.fasta")

    # Test SPOT-RNA on each sequence
    for sequence in sequences:
        dot_bracket = wrapper.fold(sequence)
        assert isinstance(dot_bracket, str)  # Ensure the structure is a string
        assert len(dot_bracket) == len(sequence)  # The structure length should match sequence length
        assert all(c in '().' for c in dot_bracket)  # Ensure the dot-bracket format is valid

if __name__ == "__main__":
    pytest.main()