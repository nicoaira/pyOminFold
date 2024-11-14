# pyrnaomnifold/core/folding_manager.py

from pyrnaomnifold.methods.rnafold.rnafold_wrapper import RNAfoldWrapper
from pyrnaomnifold.methods.linearfold.linearfold_wrapper import LinearFoldWrapper

class FoldingManager:
    def __init__(self):
        self.methods = {
            'rnafold': RNAfoldWrapper(),
            'linearfold': LinearFoldWrapper(),  # Add LinearFold as a method
            # Add other methods here as you implement them
        }

    def fold(self, method, sequence, **kwargs):
        """
        Orchestrates the folding method based on user selection.

        Args:
            method (str): Name of the folding method to use.
            sequence (str): RNA sequence to fold.
            kwargs: Optional arguments specific to each folding method.

        Returns:
            str: Predicted RNA secondary structure.
        """
        if method.lower() in self.methods:
            return self.methods[method.lower()].fold(sequence, **kwargs)
        else:
            raise ValueError(f"Method '{method}' is not supported.")