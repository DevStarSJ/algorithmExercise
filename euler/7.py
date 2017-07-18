# 10001번째의 소수

import math

def isPrime(num):
    if num == 2 or num == 3: return True
    if num % 2 == 0 or num % 3 == 0: return False

    for i in range(3,int(math.sqrt(num))+1,2):
        if num % i == 0: return False
    return True

primes = [2]
i = 3
while len(primes) < 10001:
    if isPrime(i):
        primes.append(i)
    i += 2

print(primes[10000])