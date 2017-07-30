import mathExt as M

max_count = 0

for i in range(1,1000001):
    n = M.collatz_conjecture(i)
    if n > max_count:
        max_count = n
print(max_count)