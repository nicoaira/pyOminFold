# pyrnaomnifold/methods/spotrna/spotrna_wrapper.py
import os
import subprocess
import tempfile
from pyrnaomnifold.utils.file_io import bpseq_to_dot_bracket

class SPOTRNAWrapper:
    def __init__(self):
        """
        Wrapper for SPOT-RNA, which predicts RNA secondary structure.
        """
        self.spotrna_exec = os.path.join(os.path.dirname(__file__), '../../..', 'src', 'spot-rna', 'SPOT-RNA.py')
        self.model_dir = os.path.join(os.path.dirname(__file__), '../../..', 'src', 'spot-rna', 'SPOT-RNA-models')

    def fold(self, sequence, output_dir='outputs', cpu=4, gpu=None):
        """
        Predicts the RNA secondary structure using SPOT-RNA.

        Args:
            sequence (str): RNA sequence to fold.
            output_dir (str): Directory to store output files.
            cpu (int): Number of CPUs to use for the computation.
            gpu (int, optional): GPU device ID to use for the computation.

        Returns:
            str: Predicted RNA secondary structure in dot-bracket notation.
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            # Write sequence to a temporary fasta file
            fasta_path = os.path.join(tmpdirname, 'input_sequence.fasta')
            with open(fasta_path, 'w') as fasta_file:
                fasta_file.write(">sequence\n{}\n".format(sequence))

            # Run SPOT-RNA with the generated fasta file
            output_path = os.path.join(tmpdirname, output_dir)
            os.makedirs(output_path, exist_ok=True)

            try:
                command = [
                    'python3', self.spotrna_exec,
                    '--inputs', fasta_path,
                    '--outputs', output_path,
                    '--cpu', str(cpu)
                ]
                if gpu is not None:
                    command.extend(['--gpu', str(gpu)])

                print(f"Running command: {' '.join(command)}")  # Debugging print
                subprocess.check_call(command)

                # Search for the .bpseq file in the output directory
                bpseq_file = None
                for filename in os.listdir(output_path):
                    if filename.endswith('.bpseq'):
                        bpseq_file = os.path.join(output_path, filename)
                        break

                if not bpseq_file:
                    raise FileNotFoundError("No .bpseq file found in the output directory.")

                # Extract the output from the .bpseq file
                with open(bpseq_file, 'r') as bpseq:
                    bpseq_content = bpseq.read()

                # Convert bpseq to dot-bracket notation
                dot_bracket = bpseq_to_dot_bracket(bpseq_content)

                # Adjust the length of the dot-bracket structure if needed
                if len(dot_bracket) > len(sequence):
                    dot_bracket = dot_bracket[:len(sequence)]
                elif len(dot_bracket) < len(sequence):
                    dot_bracket = dot_bracket.ljust(len(sequence), '.')

                return dot_bracket

            except subprocess.CalledProcessError as e:
                raise RuntimeError(f"SPOT-RNA failed with error: {str(e)}")

            except FileNotFoundError:
                raise FileNotFoundError("SPOT-RNA script not found or output files not generated. Make sure SPOT-RNA is installed and accessible.")
