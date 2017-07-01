#그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수

numbers = []
for i in range(2,21):
    acc = i
    for j in numbers:
        if acc % j == 0:
            acc //= j
    if acc != 1:
        numbers.append(acc)

import functools
num = functools.reduce(lambda x,y: x*y, numbers)
print(num)
