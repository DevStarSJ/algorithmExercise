from fractions import Fraction
import functional as F

result = []
result2 = []
for a in range(11, 99):
    for b in range(a + 1, 100):
        A = a / b
        if a//10 == b%10 and a * (b//10) == b * (a%10):
            result.append((a,b))
            result2.append((a%10, b//10))
        if a%10 == b//10 and a * (b%10) == b * (a//10):
            result.append((a,b))
            result2.append((a//10, b%10))

print(result, result2)
print(Fraction(F.reduce([x for x, _ in result2], lambda a,b: a * b, 1),
         F.reduce([x for _, x in result2], lambda a, b: a * b, 1)))
