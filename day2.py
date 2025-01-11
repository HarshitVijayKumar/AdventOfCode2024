from collections import defaultdict
input = []

with open("day2.txt","r") as f:
    input = f.readlines()

#Part 1
'''
answer = 0
for i in range (0,len(input)):
    line = [int(x) for x in input[i].split()]
    line_asc = sorted(line)
    line_des = sorted(line, reverse=True)
    if (line_asc!=line) and (line_des!=line):
        continue
    increasing = False
    if (line==line_asc):
        increasing = True
    valid = True
    if (increasing):
        for j in range (0,len(line)-1):
            if line[j+1]-line[j]<1 or line[j+1]-line[j]>3:
                valid = False
                break
    else:
        for j in range (0,len(line)-1):
            if line[j]-line[j+1]<1 or line[j]-line[j+1]>3:
                valid = False
                break
    if (valid):
        answer += 1

print(answer)
'''

#Part 2
'''
def isSafe(i, safe_range, allow_skip):
    prev = i[0]
    for curr in i[1:]:
        if curr-prev in safe_range:
            prev = curr
        elif not allow_skip:
            return False
        else:
            allow_skip = False
    return True


answer = 0

increasing = range(1,4)
decreasing = range(-3,0)

for i in range (0,len(input)):
    line = [int(x) for x in input[i].split()]
    answer += any([isSafe(line[1:], increasing, False), isSafe(line[1:], decreasing, False),isSafe(line, increasing, True), isSafe(line, decreasing, True)])

print(answer)
'''