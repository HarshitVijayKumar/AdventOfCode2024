import re

input = []

with open("day3.txt","r") as f:
    input = f.readlines()

#Part 1
'''
answer = 0
match_string = "mul\(\d{1,3},\d{1,3}\)"
for i in range (0,len(input)):
    multiples = re.findall(match_string,input[i])
    for j in multiples:
        L = j[4:].split(',')
        a = int(L[0])
        b = int(L[1][:len(L[1])-1])
        answer += a*b

print(answer)
'''

#Part 2
'''
answer = 0
match_string = "mul\(\d{1,3},\d{1,3}\)"
for i in range (0,len(input)):
    multiples = re.findall(match_string,input[i])
    multiples_pos = []
    dos = []
    donts = []
    L = []
    for j in multiples:
        L += [j[4:].split(',')]
    j = 0
    for j in range (0,len(input[i])-4):
        if input[i][j:j+4]=="do()":
            dos.append(j)

    for j in range (0,len(input[i])-7):
        if input[i][j:j+7]=="don't()":
            donts.append(j)

    for j in range (0,len(multiples)):
        multiples_pos.append(input[i].index(multiples[j]))

    j = 0
    enabled = True
    while (j<max(max(dos),max(donts),max(multiples_pos))+1):
        if j in dos:
            enabled = True
        if j in donts:
            enabled = False
        if not enabled:
            j += 1
        else:
            if (j in multiples_pos):
                a = int(L[multiples_pos.index(j)][0])
                b = int(L[multiples_pos.index(j)][1][:len(L[multiples_pos.index(j)][1])-1])
                print(a)
                print(b)
                answer += a*b
            j += 1

#86909417 -> high
'''