t = int(input())
Input_Guides = input().split()

x, y = 1, 1
Guide =['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for Input_Guide in Input_Guides:
    for i in range(len(Guide)):
        if Input_Guide == Guide[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > t or ny > t:
        continue

    x = nx
    y = ny

print(x, y)
