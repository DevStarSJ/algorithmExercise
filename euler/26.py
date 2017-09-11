def round_fraction(n):
    rest = []
    result = ""
    r = 1
    while True:
        r *= 10
        m = r // n
        r = (r % n)
        if (m,r) in rest:
            return int(result[rest.index((m,r)):])

        rest.append((m,r))
        result += str(m)
        if r == 0:
            return -1
    return -1

f = []
for i in range(2, 1001, 1):
    a = round_fraction(i)
    if a != -1:
        f.append((i,a))

m = max(f, key = lambda x: x[1])
print(m)


