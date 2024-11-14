# pyrnaomnifold/methods/rnafold/rnafold_wrapper.py

import RNA

class RNAfoldWrapper:
    def __init__(self):
        pass

    def fold(self, sequence):
        """
        Predicts the RNA secondary structure using ViennaRNA's RNAfold.

        Args:
            sequence (str): RNA sequence to fold.

        Returns:
            str: Predicted RNA secondary structure in dot-bracket notation.
        """
        # Use RNA.fold function from ViennaRNA to get the structure
        structure, _ = RNA.fold(sequence)  # Discard the MFE value, keep only the structure
        return structure
