import functional as F

def sum_digit_of_base(n, base):
    acc = 0
    while n >= base:
        acc += n % base
        n //= base
    acc += n
    return acc

def is_multiple(a, base):
    return a % base == 0

def brute_force_compare(m, base):
    sum_digit_of_this = F.curryr(sum_digit_of_base)(base)
    for a in range(m, 1000, m):
        is_multiple_of_num = F.curryr(is_multiple)(m)
        is_correct = F.go(a, sum_digit_of_this, is_multiple_of_num)
        if not is_correct:
            return False
    return True

def digits(base):
    result = []
    for i in range(2, base):
        if brute_force_compare(i, base):
            result.append(i)
    return result

print(digits(10))
print(digits(3))
print(digits(9))
print(digits(26))
print(digits(30))
