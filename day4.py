import re
input = []
xmas = ['X','M','A','S']

with open("day4.txt",'r') as f:
    input = f.readlines()

answer = 0

matrix = []
for i in input:
    L = [x for x in i]
    matrix.append(L)

for i in matrix:
    if '\n' in i:
        i.remove('\n')

#Part 1
'''
#Row
for i in range (0,len(input)):
    answer += len(re.findall("XMAS",input[i]))
    answer += len(re.findall("SAMX",input[i]))

for i in range (0,len(matrix)):
    for j in range (0,len(matrix[i])):
        #Column Forward
        if matrix[i][j]=='X':
            if i+3<len(matrix):
                if matrix[i+1][j]=='M' and matrix[i+2][j]=='A' and matrix[i+3][j]=='S':
                    answer += 1

        #Column Backward
        if matrix[i][j]=='S':
            if i+3<len(matrix):
                if matrix[i+1][j]=='A' and matrix[i+2][j]=='M' and matrix[i+3][j]=='X':
                    answer += 1

        #Diagonal Forward
        if matrix[i][j]=='X':
            if i+3<len(matrix) and j+3<len(matrix[i]):
                if matrix[i+1][j+1]=='M' and matrix[i+2][j+2]=='A' and matrix[i+3][j+3]=='S':
                    answer += 1

        #Diagonal Backward
        if matrix[i][j]=='S':
            if i+3<len(matrix) and j+3<len(matrix[i]):
                if matrix[i+1][j+1]=='A' and matrix[i+2][j+2]=='M' and matrix[i+3][j+3]=='X':
                    answer += 1

        #Diagonal Forward
        if matrix[i][j]=='X':
            if i+3<len(matrix) and j-3>-1:
                if matrix[i+1][j-1]=='M' and matrix[i+2][j-2]=='A' and matrix[i+3][j-3]=='S':
                    answer += 1

        #Diagonal Backward
        if matrix[i][j]=='S':
            if i+3<len(matrix) and j-3>-1:
                if matrix[i+1][j-1]=='A' and matrix[i+2][j-2]=='M' and matrix[i+3][j-3]=='X':
                    answer += 1
''' 

#Part 2
'''
for i in range (0,len(matrix)):
    for j in range (0,len(matrix[i])):
        if matrix[i][j]=='A':
            if i+1<len(matrix) and j+1<len(matrix) and i-1>-1 and j-1>-1:
                if matrix[i-1][j-1]=='M' and matrix[i+1][j+1]=='S':
                    if matrix[i-1][j+1]=='M' and matrix[i+1][j-1]=='S':
                        answer += 1
                    elif matrix[i-1][j+1]=='S' and matrix[i+1][j-1]=='M':
                        answer += 1
                elif matrix[i-1][j-1]=='S' and matrix[i+1][j+1]=='M':
                    if matrix[i-1][j+1]=='M' and matrix[i+1][j-1]=='S':
                        answer += 1
                    elif matrix[i-1][j+1]=='S' and matrix[i+1][j-1]=='M':
                        answer += 1

print(answer)
'''