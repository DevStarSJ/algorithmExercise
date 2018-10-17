checkerboard = [[-1, -1, 5, -1, -1],
                [-1, 6, 7, 0, -1],
                [3, 5, 7, 8, 2],
                [7, 6, 1, 1, 4],
                [6, 7, 4, 7, 8]]

current_x = 2
current_y = 0

def limit_x(x):
    if x < 0: return 0
    if x > 4: return 4
    return x

for y in range(1, 5):
    y_before = y - 1
    for x in range(5):
        current_weight = checkerboard[y][x]
        if current_weight == -1:
            continue

        min_weight = 99999
        #print('limit_x:', y, x, limit_x(x-1), limit_x(x+1) + 1)
        for x_before in range(limit_x(x-1), limit_x(x+1) + 1):
            before_weight = checkerboard[y_before][x_before]
            #print('before_weight :', y, x_before, before_weight)
            if before_weight == -1:
                continue

            min_weight = min(min_weight, current_weight + before_weight)
            #print(x,y, min_weight)

        if min_weight < 99999:
            checkerboard[y][x] = min_weight

print(checkerboard)














