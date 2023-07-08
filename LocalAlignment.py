import sys
import os

# Function to initialize matrices
def initialize_matrices(len_seq1, len_seq2, gap_open = -5):
    matrix_M = [[float('-inf') for j in range(len_seq2+1)] for i in range(len_seq1+1)]
    matrix_X = [[float('-inf') for j in range(len_seq2+1)] for i in range(len_seq1+1)]
    matrix_Y = [[float('-inf') for j in range(len_seq2+1)] for i in range(len_seq1+1)]
    matrix_DM = [[("graph") for j in range(len_seq2+1)] for i in range(len_seq1+1)]
    matrix_DX = [[("graph") for j in range(len_seq2+1)] for i in range(len_seq1+1)]
    matrix_DY = [[("graph") for j in range(len_seq2+1)] for i in range(len_seq1+1)]
    matrix_M[0][0] = 0
    matrix_X[0][0] = gap_open
    matrix_Y[0][0] = gap_open
    return matrix_M, matrix_X, matrix_Y, matrix_DM, matrix_DX, matrix_DY

# Function to find the match/mismatch score
def match_score(i, j, seq1, seq2):
    return 1 if seq1[i-1] == seq2[j-1] else -2

# Function to fill the matrices
def fill_matrices(matrix_M, matrix_X, matrix_Y, matrix_DM, matrix_DX, matrix_DY, seq1, seq2, gap_open=-5, gap_ext=-1):
    for i in range(len(matrix_M)):
        for j in range(len(matrix_M[i])):
            if i > 0 and j > 0:
                matrix_M[i][j] = max(matrix_M[i-1][j-1] + match_score(i, j, seq1, seq2), 
                                     matrix_X[i-1][j-1] + match_score(i, j, seq1, seq2), 
                                     matrix_Y[i-1][j-1] + match_score(i, j, seq1, seq2))

                if matrix_M[i][j] == matrix_M[i-1][j-1] + match_score(i, j, seq1, seq2):
                    matrix_DM[i][j] = "M"
                elif matrix_M[i][j] == matrix_X[i-1][j-1] + match_score(i, j, seq1, seq2):
                    matrix_DM[i][j] = "X"
                else:
                    matrix_DM[i][j] = "Y"

            if i > 0:
                matrix_X[i][j] = max(matrix_M[i-1][j] + gap_open + gap_ext, matrix_X[i-1][j] + gap_ext)

                if matrix_X[i][j] == matrix_M[i-1][j] + gap_open + gap_ext:
                    matrix_DX[i][j] = "M"
                else:
                    matrix_DX[i][j] = "X"

            if j > 0:
                matrix_Y[i][j] = max(matrix_M[i][j-1] + gap_open + gap_ext, matrix_Y[i][j-1] + gap_ext)

                if matrix_Y[i][j] == matrix_M[i][j-1] + gap_open + gap_ext:
                    matrix_DY[i][j] = "M"
                else:
                    matrix_DY[i][j] = "Y"

    return matrix_M, matrix_X, matrix_Y, matrix_DM, matrix_DX, matrix_DY

# Function to trace the path
def traceback(seq1, seq2, match_scores, x_scores, y_scores, direction_matrix):
    aligned_seq1 = []
    alignment = []
    aligned_seq2 = []

    i = len(seq1)
    j = len(seq2)

    start_score = max(match_scores[i][j], x_scores[i][j], y_scores[i][j])

    if start_score == match_scores[i][j]: 
        direction = direction_matrix[i][j]
    elif start_score == x_scores[i][j]: 
        direction = x_directions[i][j]
    elif start_score == y_scores[i][j]: 
        direction = y_directions[i][j]
        
    prev_direction = direction
    while i > 0 and j > 0:
        if prev_direction == "X": 
            if i == 1:
                aligned_seq2 += seq2[0]
                alignment += '|'
            else: 
                alignment += ' '
                aligned_seq2 += '-'
            aligned_seq1 += seq1[i-1]
            i -= 1
        elif prev_direction == "Y": 
            if j == 1:
                aligned_seq1 += seq1[0]
                alignment += '|'
            else:
                aligned_seq1 += '-'
                alignment += ' '
            aligned_seq2 += seq2[j-1]
            j -= 1
        else: 
            aligned_seq1 += seq1[i-1]
            aligned_seq2 += seq2[j-1]
            if seq1[i-1] == seq2[j-1]:
                alignment += '|'
            else:
                alignment += '*'
            j -= 1
            i -= 1
        prev_direction = direction
        direction = direction_matrix[i][j]

    aligned_seq1.reverse()
    aligned_seq1_str = ' '.join(aligned_seq1)
    
    alignment.reverse()
    alignment_str = ' '.join(alignment)
    
    aligned_seq2.reverse()
    aligned_seq2_str = ' '.join(aligned_seq2)

    return aligned_seq1_str, alignment_str, aligned_seq2_str, start_score
    
# Function to run the local sequence alignment
def sequence_alignment(seq1, seq2, gap_open = -5, ga_ext = -1):
    if not os.path.isfile(sequence_file_1) or not os.path.isfile(sequence_file_2):
        print("Both files should be in the current directory")
        return
    seq1 = list(open(seq1, "r").readline())[1:]
    seq2 = list(open(seq2, "r").readline())[1:]
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    M, X, Y, DM, DX, DY = initialize_matrices(len_seq1, len_seq2)
    fill_matrices(M, X, Y, DM, DX, DY, seq1, seq2, gap_open, ga_ext)
    seq1_aligned, seq_mid, seq2_aligned, score = traceback(seq1, seq2, M, X, Y, DM)
    print('score: ' + str(score))
    print(seq1_aligned+'\n'+seq_mid+'\n'+seq2_aligned)

if __name__ == '__main__':
    filename1 = os.path.basename(sys.argv[1])
    filename2 = os.path.basename(sys.argv[2])
    sequence_alignment(filename1, filename2)
