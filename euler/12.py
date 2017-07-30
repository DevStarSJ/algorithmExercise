import mathExt as M
import functional as F
n = 1
while F.go(n, M.triangular_number, M.divisors, len) < 500:
    n += 1
print(M.triangular_number(n))