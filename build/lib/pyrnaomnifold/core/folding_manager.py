# pyrnaomnifold/core/folding_manager.py

from pyrnaomnifold.methods.rnafold.rnafold_wrapper import RNAfoldWrapper
from pyrnaomnifold.methods.linearfold.linearfold_wrapper import LinearFoldWrapper

class FoldingManager:
    def __init__(self):
        self.methods = {
            'rnafold': RNAfoldWrapper(),
            'linearfold': LinearFoldWrapper(),  # Default to model V
        }

    def fold(self, method, sequence, **kwargs):
        """
        Orchestrates the folding method based on user selection.

        Args:
            method (str): Name of the folding method to use.
            sequence (str): RNA sequence to fold.
            kwargs (dict): Additional arguments specific to the folding method.

        Returns:
            str: Predicted RNA secondary structure in dot-bracket notation.
        """
        if method.lower() in self.methods:
            method_instance = self.methods[method.lower()]

            # Update specific attributes if any arguments are passed
            for key, value in kwargs.items():
                if hasattr(method_instance, key):
                    setattr(method_instance, key, value)

            return method_instance.fold(sequence)
        else:
            raise ValueError(f"Method '{method}' is not supported.")
