#Part 1
'''
input = []
L1 = []
L2 = []
with open("day1.txt", "r") as f:
    input = f.readlines()
for i in range (len(input)):
    line = input[i].split()
    L1.append(int(line[0]))
    L2.append(int(line[1]))
L1 = sorted(L1)
L2 = sorted(L2)
answer = 0
for i in range (len(L1)):
    answer += abs(L1[i]-L2[i])
print(answer)
'''

#Part 2
'''
input = []
L1 = []
L2 = []
with open("day1.txt", "r") as f:
    input = f.readlines()
for i in range (len(input)):
    line = input[i].split()
    L1.append(int(line[0]))
    L2.append(int(line[1]))
similarity_score = 0
for i in L1:
    similarity_score += i*L2.count(i)
print(similarity_score)
'''