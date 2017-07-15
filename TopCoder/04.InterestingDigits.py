import functional as F

def sum_digit_of_base(n, base):
    acc = 0
    while n >= base:
        acc += n % base
        n //= base
    acc += n
    return acc

is_multiple = lambda num, base: num % base == 0

def brute_force_compare(num, base):
    sum_digit_of_this = F.curryr(sum_digit_of_base)(base)
    for x in range(num, 1000, num):
        is_multiple_of_num = F.curryr(is_multiple)(num)
        if F.go(x, sum_digit_of_this, is_multiple_of_num, F.is_false): return False
    return True

def digits(base):
    return [x for x in range(2, base) if brute_force_compare(x, base)]

print(digits(10))
print(digits(3))
print(digits(9))
print(digits(26))
print(digits(30))
