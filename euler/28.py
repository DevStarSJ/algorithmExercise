def get_cross_sum(n):
    start = 1
    total = 1
    for i in range(1, n):
        step = i * 2
        start = start + step

        total += start * 4 + step * 6
        start = start + step * 3

    return total

print(get_cross_sum(501))