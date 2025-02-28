from setuptools import setup, find_packages

setup(
    name='GeneSeqX',
    version='0.1.0',
    author='xx',
    description='A bioinformatics framework for the storage, processing, analysis, and visualization of gene sequence data.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'scipy',
        'biopython',
        'requests',
        'pyyaml',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)