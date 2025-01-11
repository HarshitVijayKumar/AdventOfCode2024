import matplotlib.pyplot as plt

matrix = []
wide = 101
tall = 103

for i in range (0,wide):
    L = []
    for j in range (0,tall):
        L.append(0)
    matrix.append(L)

input = []
with open("day14.txt","r") as f:
    input = f.readlines()

speeds = dict()
pos = dict()
for i in range (0,len(input)):
    L = input[i].split()
    position = L[0][2:]
    M = position.split(',')
    pos[i] = []
    pos[i].append(int(M[0]))
    pos[i].append(int(M[1]))

    speed = L[1][2:]
    S = speed.split(',')
    speeds[i] = []
    speeds[i].append(int(S[0]))
    speeds[i].append(int(S[1]))

#Starting Positions
for i in range (0,len(input)):
    matrix[pos[i][0]][pos[i][1]] += 1

#Part 1
'''
#Updating Postions with Speed
for _ in range (0,100):
    for i in range (0,len(input)):
        cur_x = pos[i][0]
        cur_y = pos[i][1]
        matrix[pos[i][0]][pos[i][1]] -= 1
        speed_x = speeds[i][0]
        speed_y = speeds[i][1] 
        new_x = (cur_x+speed_x)%wide
        new_y = (cur_y+speed_y)%tall
        pos[i][0] = new_x
        pos[i][1] = new_y
        matrix[new_x][new_y] += 1

safety_score_1 = 0
safety_score_2 = 0
safety_score_3 = 0
safety_score_4 = 0

for i in range (0,int(wide/2)):
    for j in range (0,int(tall/2)):
        safety_score_1 += matrix[i][j]
        safety_score_2 += matrix[51+i][j]
        safety_score_3 += matrix[i][52+j]
        safety_score_4 += matrix[51+i][52+j]

print(safety_score_1*safety_score_2*safety_score_3*safety_score_4)
'''

#Part 2

#Updating Postions with Speed
for k in range (0,7500):
    for i in range (0,len(input)):
        cur_x = pos[i][0]
        cur_y = pos[i][1]
        matrix[pos[i][0]][pos[i][1]] -= 1
        speed_x = speeds[i][0]
        speed_y = speeds[i][1] 
        new_x = (cur_x+speed_x)%wide
        new_y = (cur_y+speed_y)%tall
        pos[i][0] = new_x
        pos[i][1] = new_y
        matrix[new_x][new_y] += 1

for k in range (0,2500):
    for i in range (0,len(input)):
        cur_x = pos[i][0]
        cur_y = pos[i][1]
        matrix[pos[i][0]][pos[i][1]] -= 1
        speed_x = speeds[i][0]
        speed_y = speeds[i][1] 
        new_x = (cur_x+speed_x)%wide
        new_y = (cur_y+speed_y)%tall
        pos[i][0] = new_x
        pos[i][1] = new_y
        matrix[new_x][new_y] += 1

    plt.imshow(matrix)
    plt.savefig(str(k)+".png")
    