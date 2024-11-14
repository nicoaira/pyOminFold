# pyrnaomnifold/methods/linearfold/linearfold_wrapper.py

import subprocess

class LinearFoldWrapper:
    def __init__(self, model='V'):
        """
        Initializes the LinearFoldWrapper.

        Args:
            model (str): Specifies which LinearFold model to use ('V' for ViennaRNA, 'C' for CONTRAfold).
                         Default is 'V'.
        """
        if model not in ['V', 'C']:
            raise ValueError("Model must be either 'V' (ViennaRNA) or 'C' (CONTRAfold).")
        self.model = model

    def fold(self, sequence):
        """
        Predicts the RNA secondary structure using LinearFold.

        Args:
            sequence (str): RNA sequence to fold.

        Returns:
            str: Predicted RNA secondary structure in dot-bracket notation.
        """
        # Determine which model to use
        model_flag = '-V' if self.model == 'V' else '-C'

        # Run the LinearFold executable using subprocess
        try:
            result = subprocess.run(
                ['linearfold', model_flag],
                input=sequence.encode(),
                text=True,
                capture_output=True,
                check=True
            )
            # Parse the output to extract the structure
            structure = result.stdout.splitlines()[-1]  # Assuming the structure is the last line in the output
            return structure
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"LinearFold failed to run: {e}")

