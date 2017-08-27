import mathExt as M

abundant_numbers = []
not_two_abundants = []

for i in range(1, 28124):
    if M.is_abundant_number(i):
        abundant_numbers.append(i)
    is_in = False
    for j in abundant_numbers:
        k = i - j
        if k > 0 and k in abundant_numbers:
            is_in = True
            break
    if not is_in:
        print(i)
        not_two_abundants.append(i)

print(sorted(not_two_abundants))
print(sum(not_two_abundants))

