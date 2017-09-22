import math

factorials = [math.factorial(x) for x in range(0,10)]

result = []
for x in range(11, 1000000):
    if sum([factorials[int(a)] for a in str(x)]) == x:
        result.append(x)

print(result)
print(sum(result))
