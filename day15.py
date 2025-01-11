warehouse = []

moves = []

input = []

with open("day15.txt",'r') as f:
    input = f.readlines()

i = 0
while input[i]!='\n':
    warehouse.append(input[i])
    i += 1
i += 1
while (i<len(input)):
    moves.append(input[i])
    i += 1

cur_x = -1
cur_y = -1

for i in range (0,len(warehouse)):
    L = []
    for j in range (0,len(warehouse[i])):
        if warehouse[i][j]=='#':
            L.append('#')
            L.append('#')
        elif warehouse[i][j]=='O':
            L.append('[')
            L.append(']')
        elif warehouse[i][j]=='.':
            L.append('.')
            L.append('.')
        else:
            L.append('@')
            L.append('.')
        if warehouse[i][j] == '@':
            cur_x = i
            cur_y = j
    if '\n' in L:
        L.remove('\n')
    warehouse[i] = L

for i in range (0,len(moves)):
    L = []
    for j in range (0,len(moves[i])):
        L.append(moves[i][j])
    if '\n' in L:
        L.remove('\n')
    moves[i] = L

#Part 1
'''
for i in range (0,len(moves)):
    for j in range (0,len(moves[i])):
        if (moves[i][j]=='>'):
            start = cur_y
            end = cur_y+1
            if warehouse[cur_x][end]=='#':
                continue
            elif warehouse[cur_x][end]=='.':
                warehouse[cur_x][cur_y]='.'
                warehouse[cur_x][end]='@'
                cur_y = cur_y+1
            else:
                end += 1
                while (end+1<len(warehouse[cur_x])):
                    if warehouse[cur_x][end]=='#':
                        break
                    if warehouse[cur_x][end]=='.':
                        warehouse[cur_x][cur_y] = '.'
                        warehouse[cur_x][cur_y+1] = '@'
                        cur_y = cur_y + 1
                        warehouse[cur_x][end] = 'O'
                        break
                    end += 1
        elif (moves[i][j]=='<'):
            start = cur_y
            end = cur_y-1
            if warehouse[cur_x][end]=='#':
                continue
            elif warehouse[cur_x][end]=='.':
                warehouse[cur_x][cur_y]='.'
                warehouse[cur_x][end]='@'
                cur_y = cur_y-1
            else:
                end -= 1
                while (end-1>-1):
                    if warehouse[cur_x][end]=='#':
                        break
                    if warehouse[cur_x][end]=='.':
                        warehouse[cur_x][cur_y] = '.'
                        warehouse[cur_x][cur_y-1] = '@'
                        cur_y = cur_y - 1
                        warehouse[cur_x][end] = 'O'
                        break
                    end -= 1
        elif (moves[i][j]=='^'):
            start = cur_x
            end = cur_x-1
            if warehouse[end][cur_y]=='#':
                continue
            elif warehouse[end][cur_y]=='.':
                warehouse[cur_x][cur_y]='.'
                warehouse[end][cur_y]='@'
                cur_x = cur_x-1
            else:
                end -= 1
                while (end-1>-1):
                    if warehouse[end][cur_y]=='#':
                        break
                    if warehouse[end][cur_y]=='.':
                        warehouse[cur_x][cur_y] = '.'
                        warehouse[cur_x-1][cur_y] = '@'
                        cur_x = cur_x - 1
                        warehouse[end][cur_y] = 'O'
                        break
                    end -= 1
        elif (moves[i][j]=='v'):
            start = cur_x
            end = cur_x+1
            if warehouse[end][cur_y]=='#':
                continue
            elif warehouse[end][cur_y]=='.':
                warehouse[cur_x][cur_y]='.'
                warehouse[end][cur_y]='@'
                cur_x = cur_x+1
            else:
                end += 1
                while (end+1<len(warehouse[cur_x])):
                    if warehouse[end][cur_y]=='#':
                        break
                    if warehouse[end][cur_y]=='.':
                        warehouse[cur_x][cur_y] = '.'
                        warehouse[cur_x+1][cur_y] = '@'
                        cur_x = cur_x + 1
                        warehouse[end][cur_y] = 'O'
                        break
                    end += 1

answer = 0

for i in range (0,len(warehouse)):
    for j in range (0,len(warehouse[i])):
        if warehouse[i][j] == 'O':
            answer += 100*i+j

print(answer)

'''

#Part 2

for i in range (0,len(moves)):
    for j in range (0,len(moves[i])):
        if (moves[i][j]=='>'):
            start = cur_y
            end = cur_y+1
            if warehouse[cur_x][end]=='#':
                continue
            elif warehouse[cur_x][end]=='.':
                warehouse[cur_x][cur_y]='.'
                warehouse[cur_x][end]='@'
                cur_y = cur_y+1
            else:
                end += 1
                while (end+1<len(warehouse[cur_x])):
                    if warehouse[cur_x][end]=='#':
                        break
                    if warehouse[cur_x][end]=='.':
                        for k in range (end, start,-1):
                            temp = warehouse[cur_x][k]
                            warehouse[cur_x][k] = warehouse[cur_x][k-1]
                            warehouse[cur_x][k-1] = temp
                        cur_y = cur_y + 1
                        break
                    end += 1
        elif (moves[i][j]=='<'):
            start = cur_y
            end = cur_y-1
            if warehouse[cur_x][end]=='#':
                continue
            elif warehouse[cur_x][end]=='.':
                warehouse[cur_x][cur_y]='.'
                warehouse[cur_x][end]='@'
                cur_y = cur_y-1
            else:
                end -= 1
                while (end-1>-1):
                    if warehouse[cur_x][end]=='#':
                        break
                    if warehouse[cur_x][end]=='.':
                        for k in range (end, start):
                            temp = warehouse[cur_x][k]
                            warehouse[cur_x][k] = warehouse[cur_x][k+1]
                            warehouse[cur_x][k+1] = temp
                        cur_y = cur_y - 1
                        break
                    end -= 1
        elif (moves[i][j]=='^'):
            start = cur_x
            end = cur_x-1
            if warehouse[end][cur_y]=='#':
                continue
            elif warehouse[end][cur_y]=='.':
                warehouse[cur_x][cur_y]='.'
                warehouse[end][cur_y]='@'
                cur_x = cur_x-1
            else:
                valid = True
                blocks = []
                all_blocks = []
                end -= 1
                if warehouse[end][cur_y] == '[':
                    blocks.append(end)
                    blocks.append(end+1)
                else:
                    blocks.append(end)
                    blocks.append(end-1)
                while (len(blocks)!=0):
                    cur_block = blocks.pop(0)
                    all_blocks.append(cur_block)
                    if warehouse[cur_block-1][cur_y]=='#':
                        valid = False
                        blocks = []
                    elif warehouse[cur_block-1][cur_y]=='[' :
                        if cur_block-1 not in blocks:
                            blocks.append(cur_block-1)
                print(blocks)
        elif (moves[i][j]=='v'):
            start = cur_x
            end = cur_x+1
            if warehouse[end][cur_y]=='#':
                continue
            elif warehouse[end][cur_y]=='.':
                warehouse[cur_x][cur_y]='.'
                warehouse[end][cur_y]='@'
                cur_x = cur_x+1
            else:
                end += 1
                while (end+1<len(warehouse[cur_x])):
                    if warehouse[end][cur_y]=='#':
                        break
                    if warehouse[end][cur_y]=='.':
                        warehouse[cur_x][cur_y] = '.'
                        warehouse[cur_x+1][cur_y] = '@'
                        cur_x = cur_x + 1
                        warehouse[end][cur_y] = 'O'
                        break
                    end += 1

answer = 0

for i in range (0,len(warehouse)):
    for j in range (0,len(warehouse[i])):
        if warehouse[i][j] == 'O':
            answer += 100*i+j

print(answer)
