import mathExt as M

def get_prime_nums(a, b):
    primes = 0
    i = 0
    while True:
        n = i*i + a * i + b
        if n < 1:
            return 0
        if M.is_prime(n):
            primes += 1
        else:
            return primes
        i += 1

max_primes = 0
max_ab = 0

for a in range(-1000,1001):
    for b in range(-1000,1001):
        n = get_prime_nums(a, b)
        if n > max_primes:
            max_primes = n
            max_ab = a * b
print(max_primes, max_ab)