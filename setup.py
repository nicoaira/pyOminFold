from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import os
import sys

class CustomInstallCommand(install):
    """Customized setuptools install command to build LinearFold and download SPOT-RNA weights."""

    def run(self):
        # Compile LinearFold source code during the installation
        try:
            linearfold_path = os.path.join(os.path.dirname(__file__), 'src', 'linearfold')
            subprocess.check_call(['make'], cwd=linearfold_path)
        except subprocess.CalledProcessError as e:
            raise RuntimeError("Failed to compile LinearFold. Make sure you have 'make' and necessary tools installed.")

        # Download and extract SPOT-RNA models
        try:
            spotrna_model_url_1 = 'https://www.dropbox.com/s/dsrcf460nbjqpxa/SPOT-RNA-models.tar.gz'
            spotrna_model_url_2 = 'https://app.nihaocloud.com/f/fbf3315a91d542c0bdc2/?dl=1'
            model_path = os.path.join(os.path.dirname(__file__), 'src', 'spot-rna')
            os.makedirs(model_path, exist_ok=True)

            # Try to download SPOT-RNA models
            subprocess.check_call(['wget', spotrna_model_url_1, '-O', 'SPOT-RNA-models.tar.gz'], cwd=model_path)
        except subprocess.CalledProcessError:
            # Fallback URL
            subprocess.check_call(['wget', '-O', 'SPOT-RNA-models.tar.gz', spotrna_model_url_2], cwd=model_path)

        # Extract the downloaded models and remove the tar file
        subprocess.check_call(['tar', '-xvzf', 'SPOT-RNA-models.tar.gz'], cwd=model_path)
        os.remove(os.path.join(model_path, 'SPOT-RNA-models.tar.gz'))

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
        'ViennaRNA',
        'pandas',
        'tqdm',
        'argparse',
        'six',
        'tensorflow',
        # Adding dependencies from the provided .yml file (without version numbers)
        'asttokens',
        'backcall',
        'bottleneck',
        'certifi',
        'charset-normalizer',
        'debugpy',
        'decorator',
        'entrypoints',
        'executing',
        'ffmpeg',
        'gmp',
        'idna',
        'intel-openmp',
        'ipykernel',
        'ipython',
        'jedi',
        'joblib',
        'jpeg',
        'jupyter_client',
        'jupyter_core',
        'lame',
        'lcms2',
        'lerc',
        'libdeflate',
        'libffi',
        'libgfortran-ng',
        'libgfortran5',
        'libgomp',
        'libiconv',
        'libpng',
        'libsodium',
        'libstdcxx-ng',
        'libtiff',
        'libuv',
        'libwebp-base',
        'lz4-c',
        'matplotlib-inline',
        'mkl',
        'mkl-service',
        'mkl_fft',
        'mkl_random',
        'ncurses',
        'nest-asyncio',
        'nettle',
        'numexpr',
        'numpy-base',
        'olefile',
        'openh264',
        'openjpeg',
        'openssl',
        'packaging',
        'parso',
        'pexpect',
        'pickleshare',
        'pillow',
        'pip',
        'platformdirs',
        'pooch',
        'prompt-toolkit',
        'psutil',
        'ptyprocess',
        'pure_eval',
        'pygments',
        'python-dateutil',
        'python-tzdata',
        'python_abi',
        'pytorch',
        'pytorch-mutex',
        'pytz',
        'pyzmq',
        'readline',
        'requests',
        'scikit-learn',
        'scipy',
        'setuptools',
        'stack_data',
        'threadpoolctl',
        'tk',
        'torchaudio',
        'torchvision',
        'tornado',
        'traitlets',
        'typing_extensions',
        'urllib3',
        'wcwidth',
        'wheel',
        'xz',
        'zeromq',
        'zlib',
        'zstd',
        # pip-only dependencies
        'antlr4-python3-runtime',
        'bitarray',
        'cffi',
        'colorama',
        'cython',
        'fairseq',
        'hydra-core',
        'lxml',
        'omegaconf',
        'portalocker',
        'protobuf',
        'pycparser',
        'pyyaml',
        'regex',
        'sacrebleu',
        'tabulate',
        'tensorboardx',
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
