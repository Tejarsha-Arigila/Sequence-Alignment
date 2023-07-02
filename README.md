# Sequence Alignment Toolkit

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)

Welcome to the Sequence-Alignment-Toolkit repository. Here you will find a Python implementation for performing sequence alignment. Sequence alignment is a method of arranging sequences of DNA, RNA, or protein to identify regions of similarity. These similarities could be the result of functional, structural, or evolutionary relationships between the sequences.

This repository provides scripts for two types of sequence alignments: Global Alignment and Local Alignment. Each script calculates the match score between two sequences, aiding in the understanding of their comparative structures.

## Included Files
- `GlobalAlignment.py`: Executes a global sequence alignment without an affine gap penalty.
- `LocalAlignment.py`: Executes a local sequence alignment incorporating an affine gap penalty.
- `seq1.fa`: Contains a sample sequence for testing (FASTA format).
- `seq2.fa`: Contains a second sample sequence for testing (FASTA format).

> Note: The FASTA file format should follow the structure `>Sequence` (e.g., `>AGCTAGC`).

## Execution Instructions
To run the scripts, follow these steps:

1. Navigate to the directory containing the files.
2. Place your target sequences in `seq1.fa` and `seq2.fa` respectively, using the format specified above.
3. Open your terminal and navigate to the directory of this repository.
4. Run the scripts with the following commands:
    - For Global Alignment: `python GlobalAlignment.py seq1.fa seq2.fa`
    - For Local Alignment: `python LocalAlignment.py seq1.fa seq2.fa`

Please ensure that you have Python installed in your environment before executing these scripts.

Enjoy exploring the wonders of sequence alignment!
