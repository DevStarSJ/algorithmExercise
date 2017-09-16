import math

result = set()

for a in range(2,101):
    for b in range(2,101):
        result.add(math.pow(a,b))

print(len(result))
