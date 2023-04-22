import sys

# Function to initialize matrices
def initialize_matrix(seq_1, seq_2):
    matrix = [[0 for x in range(len(seq_2)+1)] for x in range(len(seq_1)+1)]
    direction = [["A" for x in range(len(seq_2)+1)] for x in range(len(seq_1)+1)]
    return matrix, direction

# Function to find the match/mismatch score
def match_score(i, j, seq_1, seq_2):
    return 1 if seq_1[i-1] == seq_2[j-1] else -2

# Function to fill the matrices
def fill_matrix(matrix, direction, seq_1, seq_2, gap=-3):
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[i])):
            matrix[i][j] = max(matrix[i][j-1] + gap,
                          matrix[i-1][j] + gap,
                          matrix[i-1][j-1] + match_score(i,j,seq_1,seq_2))
            if (seq_1[i-1] == seq_2[j-1]):
                if (matrix[i][j] == matrix[i][j-1]+gap):
                    direction[i][j] = "L"
                elif (matrix[i][j] == matrix[i-1][j-1]+match_score(i,j,seq_1,seq_2)):
                    direction[i][j] = "D"
                else:
                    direction[i][j] = "U"
            elif (i == len(matrix)-1 and j == len(matrix[i])-1):
                direction[i][j] = "D"
            else:
                if (matrix[i][j] == matrix[i][j-1]+gap):
                    direction[i][j] = "L"
                elif (matrix[i][j] == matrix[i-1][j]+gap):
                    direction[i][j] = "U"
                else:
                    direction[i][j] = "D"
    return matrix, direction

# Function to trace the path
def trace_matrix(matrix, direction, seq_1, seq_2):
    seq_1_align = []
    seq_mid = []
    seq_2_align = []
    j = len(seq_2)
    i = len(seq_1)
    prev_direction = direction[i][j]
    while(i>0 or j>0):
        if prev_direction == "D":
            seq_1_align += seq_1[i-1]
            if (seq_1[i-1] == seq_2[j-1]):
                seq_mid += '|'
            else:
                seq_mid += '*'
            seq_2_align += seq_2[j-1]
            j = j-1
            i = i-1
        elif prev_direction == "L" or prev_direction == "A":
            seq_1_align += '-'
            seq_mid += ' '
            seq_2_align += seq_2[j-1]
            j = j - 1
        else:
            seq_1_align += seq_1[i-1]
            seq_mid += ' '
            seq_2_align += '-'
            i = i - 1
        prev_direction = direction[i][j]
    seq_1_align.reverse()
    seq_2_align.reverse()
    seq_mid.reverse()
    return seq_1_align, seq_mid, seq_2_align

# Function to run the global sequence alignment
def sequence_alignment(sequence_file_1, sequence_file_2):
    seq_1 = list(open(sequence_file_1, "r").readline())[1:]
    seq_2 = list(open(sequence_file_2, "r").readline())[1:]
    alignment_matrix, direction_matrix = initialize_matrix(seq_1, seq_2)
    alignment_matrix, direction_matrix = fill_matrix(alignment_matrix, direction_matrix, seq_1, seq_2)
    aligned_seq_1, alignment_mid, aligned_seq_2 = trace_matrix(alignment_matrix, direction_matrix, seq_1, seq_2)
    print('Score : ' + str(alignment_matrix[-1][-1]))
    print(' '.join(aligned_seq_1)+'\n'+' '.join(alignment_mid)+'\n'+' '.join(aligned_seq_2))
    
if __name__ == '__main__':
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    sequence_alignment(filename1, filename2)