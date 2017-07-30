space = [[1 for _ in range(21)] for _ in range(21)]

for x in range(1,21):
    for y in range(1,21):
        space[x][y] = space[x-1][y] + space[x][y-1]

print(space[20][20])
