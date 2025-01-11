from math import sqrt
input = []

with open("day6.txt",'r') as f:
    input = f.readlines()

matrix = []

for i in range (0,len(input)):
    L = [x for x in input[i]]
    if '\n' in L:
        L.remove('\n')
    matrix.append(L)

cur_x = -1
cur_y = -1

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[i])):
        if matrix[i][j]=='^':
            cur_x = i
            cur_y = j

#Part 1
'''
while (True):
    if (matrix[cur_x][cur_y]=='^'):
        if cur_x-1<=-1:
            break
        if matrix[cur_x-1][cur_y] == '#':
            matrix[cur_x][cur_y] = '>'
        else:
            matrix[cur_x][cur_y] = 'X'
            matrix[cur_x-1][cur_y] = '^'
            cur_x = cur_x - 1
    elif (matrix[cur_x][cur_y]=='>'):
        if cur_y+1>=len(matrix[cur_x]):
            break
        if matrix[cur_x][cur_y+1] == '#':
            matrix[cur_x][cur_y] = 'v'
        else:  
            matrix[cur_x][cur_y] = 'X'
            matrix[cur_x][cur_y+1] = '>'
            cur_y = cur_y + 1
    elif (matrix[cur_x][cur_y]=='v'):
        if cur_x+1>=len(matrix):
            break
        if matrix[cur_x+1][cur_y] == '#':
            matrix[cur_x][cur_y] = '<'
        else:   
            matrix[cur_x][cur_y] = 'X'
            matrix[cur_x+1][cur_y] = 'v'
            cur_x = cur_x + 1
    elif (matrix[cur_x][cur_y]=='<'):
        if cur_y-1<=-1:
            break
        if matrix[cur_x][cur_y-1] == '#':
            matrix[cur_x][cur_y] = '^'
        else:
            matrix[cur_x][cur_y] = 'X'
            matrix[cur_x][cur_y-1] = '<'
            cur_y = cur_y - 1

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[i])):
        if matrix[i][j]=='^' or matrix[i][j]=='>' or matrix[i][j]=='v' or matrix[i][j]=='^':
            matrix[cur_x][cur_y]='X'

answer = 0

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[i])):
        if matrix[i][j]=='X':
            answer += 1

print(answer)
'''

#Part 2
answer = 0
coordinates = []

while (True):
    if (matrix[cur_x][cur_y]=='^'):
        if cur_x-1<=-1:
            break
        if matrix[cur_x-1][cur_y] == '#':
            matrix[cur_x][cur_y] = '>'
            coordinates.append([cur_x+1,cur_y])
        else:
            matrix[cur_x][cur_y] = 'X'
            matrix[cur_x-1][cur_y] = '^'
            cur_x = cur_x - 1
    elif (matrix[cur_x][cur_y]=='>'):
        if cur_y+1>=len(matrix[cur_x]):
            break
        if matrix[cur_x][cur_y+1] == '#':
            matrix[cur_x][cur_y] = 'v'
            coordinates.append([cur_x, cur_y-1])
        else:  
            matrix[cur_x][cur_y] = 'X'
            matrix[cur_x][cur_y+1] = '>'
            cur_y = cur_y + 1
    elif (matrix[cur_x][cur_y]=='v'):
        if cur_x+1>=len(matrix):
            break
        if matrix[cur_x+1][cur_y] == '#':
            matrix[cur_x][cur_y] = '<'
            coordinates.append([cur_x-1, cur_y])
        else:   
            matrix[cur_x][cur_y] = 'X'
            matrix[cur_x+1][cur_y] = 'v'
            cur_x = cur_x + 1
    elif (matrix[cur_x][cur_y]=='<'):
        if cur_y-1<=-1:
            break
        if matrix[cur_x][cur_y-1] == '#':
            matrix[cur_x][cur_y] = '^'
            coordinates.append([cur_x, cur_y+1])
        else:
            matrix[cur_x][cur_y] = 'X'
            matrix[cur_x][cur_y-1] = '<'
            cur_y = cur_y - 1

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[i])):
        if matrix[i][j]=='^' or matrix[i][j]=='>' or matrix[i][j]=='v' or matrix[i][j]=='^':
            matrix[cur_x][cur_y]='X'
            coordinates.append([cur_x, cur_y])

answer = 0

for i in range (0,len(coordinates)-4):
    perimeter_1 = sqrt((coordinates[i+1][0]-coordinates[i][0])**2+(coordinates[i+1][1]-coordinates[i][1])**2)
    perimeter_2 = sqrt((coordinates[i+2][0]-coordinates[i+1][0])**2+(coordinates[i+2][1]-coordinates[i+1][1])**2)
    perimeter_3 = sqrt((coordinates[i+3][0]-coordinates[i+2][0])**2+(coordinates[i+3][1]-coordinates[i+2][1])**2)

    if perimeter_3>=perimeter_1:
        answer += 1

print(answer)