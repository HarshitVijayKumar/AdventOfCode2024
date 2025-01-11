from collections import defaultdict
test_values = []
inputs = []

with open ("day7.txt",'r') as f:
    inputs = f.readlines()

test_values = [int(x.split(':')[0]) for x in inputs]
inputs = [x.split(':')[1].split() for x in inputs]

for i in range(0,len(inputs)):
    for j in range (0,len(inputs[i])):
        inputs[i][j] = int(inputs[i][j])

valid = []
for i in range(0,len(test_values)):
    valid.append(False)


d = defaultdict(list)
options = defaultdict(list)

def evaluate(s, input):
    print(s)
    i = 0
    while (len(input)!=1):
        a = input.pop(1)
        b = input.pop(0)
        if s[i]=='+':
            input.insert(0,a+b)
        else:
            input.insert(0,a*b)
        i += 1
    return (input[0])

def createExpression(s, input, n, i):
    valid = True
    for i in s:
        if len(i)<len(input)-1:
            valid = False
    if (valid):
        options[len(input)] = s
        return
    element = s.pop(0)
    if element < len(input)-1:
        s.append(element + '+')
        s.append(element + '*')
    else:
        s.append(element)

for i in range (0,len(inputs)):
    if len(options[len(inputs[i])])==0:
        createExpression([], inputs[i], 0, i)

print(options)
'''
answer = 0

for i in range (0,len(inputs)):
    if test_values[i] in d[i]:
        answer += test_values[i]

print(d)
'''