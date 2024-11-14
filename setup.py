from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import os

class CustomInstallCommand(install):
    """Customized setuptools install command to build LinearFold."""

    def run(self):
        # Compile LinearFold source code during the installation
        try:
            linearfold_path = os.path.join(os.path.dirname(__file__), 'src', 'linearfold')
            subprocess.check_call(['make'], cwd=linearfold_path)
        except subprocess.CalledProcessError as e:
            raise RuntimeError("Failed to compile LinearFold. Make sure you have 'make' and necessary tools installed.")

        # Run the standard install command
        install.run(self)

setup(
    name='pyRNAOmniFold',
    version='0.1.0',
    description='pyRNAOmniFold: A comprehensive suite for RNA secondary structure prediction',
    author='Nicolas Aira',
    author_email='naira@uic.es',
    url='https://github.com/yourusername/pyRNAOmniFold',  # Replace with actual URL
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    keywords='RNA secondary structure prediction bioinformatics',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'biopython',
        'ViennaRNA'
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
    entry_points={
        'console_scripts': [
            'pyrnaomnifold = pyrnaomnifold.cli:main',
        ],
    },
    python_requires='>=3.8',
)
