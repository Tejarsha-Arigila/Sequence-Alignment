# Sequence-Alignment

This Repository contains python implementation to perform sequence alignment and calculate match score of two sequences.

Filenames:

- GlobalAlignment.py: without affine gap penalty.
- LocalAlignment.py: with affine gap penalty.
- seq1.fa: Sample 1 FASTA file. 
- seq2.fa: Sample 2 FASTA file. 

Note: Format of FASTA File is >Sequence (Ex. >AGCTAGC).

# How to run:
- Go to the the directory of this folder.
- Paste the sequences in seq1.fa and seq2.fa as mentioned.
- Open Terminal.
- Go to the the directory of this folder.
- Use following syntax to run the python scripts: 
    - python LocalAlignment.py seq1.fa seq2.fa
    - python GlobalAlignment.py seq1.fa seq2.fa
