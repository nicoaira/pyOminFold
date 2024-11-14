# tests/test_linearfold.py
import pytest
from pyrnaomnifold.methods.linearfold.linearfold_wrapper import LinearFoldWrapper

from pyrnaomnifold.utils.file_io import read_fasta_sequences

def test_linearfold_wrapper():
    # Initialize LinearFold wrapper with default model 'V'
    wrapper = LinearFoldWrapper(model='V')

    # Load test sequences from the FASTA file
    sequences = read_fasta_sequences("tests/test_sequences.fasta")

    # Test LinearFold on each sequence
    for sequence in sequences:
        structure = wrapper.fold(sequence)
        assert isinstance(structure, str)  # Ensure the structure is a string
        assert len(structure) == len(sequence)  # The structure length should match sequence length

    # Initialize LinearFold wrapper with model 'C'
    wrapper = LinearFoldWrapper(model='C')

    # Test LinearFold on each sequence
    for sequence in sequences:
        structure = wrapper.fold(sequence)
        assert isinstance(structure, str)  # Ensure the structure is a string
        assert len(structure) == len(sequence)  # The structure length should match sequence length