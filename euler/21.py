import mathExt as M

result = []

for i in range(2, 10001):
    if M.is_amicable(i):
        result.append(i)

print(sum(result))
