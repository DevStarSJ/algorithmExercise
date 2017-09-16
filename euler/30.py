import math

def digit_pow(n,b):
    return sum([math.pow(int(i),b) for i in str(n)])

result = []
for i in range(2, 1000000):
    if i == digit_pow(i,5):
        result.append(i)

print(sum(result))
