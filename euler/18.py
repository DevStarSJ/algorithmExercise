import functional as F

triangle = [
"75",
"95 64",
"17 47 82",
"18 35 87 10",
"20 04 82 47 65",
"19 01 23 75 03 34",
"88 02 77 73 07 63 67",
"99 65 04 28 06 16 70 92",
"41 41 26 56 83 40 80 70 33",
"41 48 72 33 47 32 37 16 94 29",
"53 71 44 65 25 43 91 52 97 51 14",
"70 11 33 28 77 73 17 78 39 68 17 57",
"91 71 52 38 17 14 91 43 58 50 27 29 48",
"63 66 04 68 89 53 67 30 73 16 69 87 40 31",
"04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
]
triangle = F.map(triangle, lambda y: [int(x) for x in y.split(' ')])

def get_upper(x, y):
    pos_y = y - 1
    start_x = 0 if x < 1 else x - 1
    prev_x_len = len(triangle[pos_y])
    end_x = min([x, prev_x_len])
    return max(triangle[pos_y][start_x:end_x + 1])

for y in range(1, len(triangle)):
    for x in range(len(triangle[y])):
        triangle[y][x] += get_upper(x, y)

print(max(triangle[-1]))
