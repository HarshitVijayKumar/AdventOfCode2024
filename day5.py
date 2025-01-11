from collections import defaultdict
input = []

with open("day5.txt",'r') as f:
    input = f.readlines()

rules = []
i = 0
while (input[i]!='\n'):
    L = []
    L.append(int(input[i][0:2]))
    L.append(int(input[i][3:5]))
    i += 1
    rules.append(L)
i += 1

pages = []
while (i<len(input)):
    L = [int(x) for x in input[i].split(',')]
    pages.append(L)
    i += 1

#Part 1
'''
answer = 0
for i in range (0,len(pages)):
    valid = True
    for j in range (0,len(rules)):
        if rules[j][0] in pages[i] and rules[j][1] in pages[i]:
            if pages[i].index(rules[j][1])<pages[i].index(rules[j][0]):
                 valid = False
    if valid:
        answer += pages[i][int(len(pages[i])/2)]
print(answer)
'''

#Part 2
'''
answer = 0
for i in range (0,len(pages)):
    valid = False
    changed = True
    while (changed):
        changed = False
        for j in range (0,len(rules)):
            if rules[j][0] in pages[i] and rules[j][1] in pages[i]:
                if pages[i].index(rules[j][1])<pages[i].index(rules[j][0]):
                    a = pages[i].index(rules[j][1])
                    b = pages[i].index(rules[j][0])
                    t = pages[i][a]
                    pages[i][a] = pages[i][b]
                    pages[i][b] = t
                    valid = True
                    changed = True
    if valid:
        answer += pages[i][int(len(pages[i])/2)]
print(answer)
'''