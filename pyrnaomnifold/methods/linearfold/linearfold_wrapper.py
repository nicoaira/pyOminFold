# pyrnaomnifold/methods/linearfold/linearfold_wrapper.py
import subprocess
import os

class LinearFoldWrapper:
    def __init__(self, model='C'):
        """
        Wrapper for LinearFold, which predicts RNA secondary structure.

        Args:
            model (str): LinearFold model to use. Options are 'V' (default) or 'C'.
        """
        if model not in ['V', 'C']:
            raise ValueError("Model must be either 'V' (Vienna) or 'C' (CONTRAfold). Default is 'C'.")
        self.model = model

    def fold(self, sequence):
        """
        Predicts the RNA secondary structure using LinearFold.

        Args:
            sequence (str): RNA sequence to fold.

        Returns:
            str: Predicted RNA secondary structure in dot-bracket notation.
        """
        linearfold_path = os.path.join(os.path.dirname(__file__), '../../..', 'src', 'linearfold', 'linearfold')
        command = [linearfold_path]

        # Add model-specific argument
        if self.model == 'V':
            command.append('-V')

        # Execute LinearFold with the provided sequence
        try:
            process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate(input=sequence.encode())

            if process.returncode != 0:
                raise RuntimeError(f"LinearFold failed with error: {stderr.decode().strip()}")

            # The output contains the structure and energy, we need to extract just the structure
            output_lines = stdout.decode().split('\n')
            for line in output_lines:
                if '(' in line or '.' in line:
                    # Split by whitespace to discard the energy value and keep only the structure
                    return line.split()[0].strip()
            raise RuntimeError("Failed to extract RNA secondary structure from LinearFold output.")

        except FileNotFoundError:
            raise FileNotFoundError("LinearFold binary not found. Make sure it is compiled and accessible.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while running LinearFold: {str(e)}")
