# tests/test_folding_manager.py
import pytest
from pyrnaomnifold.core.folding_manager import FoldingManager
from pyrnaomnifold.utils.file_io import read_fasta_sequences

def test_folding_manager():
    # Initialize FoldingManager
    manager = FoldingManager()

    # Load test sequences from the FASTA file
    sequences = read_fasta_sequences("tests/test_sequences.fasta")

    # Test FoldingManager with each method and each sequence
    methods = ['rnafold', 'linearfold', 'spotrna']

    for method in methods:
        for sequence in sequences:
            dot_bracket = manager.fold(method, sequence)
            assert isinstance(dot_bracket, str)  # Ensure the structure is a string
            assert len(dot_bracket) == len(sequence)  # The structure length should match sequence length
            assert all(c in '().' for c in dot_bracket)  # Ensure the dot-bracket format is valid

if __name__ == "__main__":
    pytest.main()
