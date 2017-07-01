#이백만(2,000,000) 이하 소수의 합

import math

def isPrime(num):
    if num == 2 or num == 3: return True
    if num % 2 == 0 or num % 3 == 0: return False

    for i in range(3,int(math.sqrt(num))+1,2):
        if num % i == 0: return False
    return True

primes = [2] + [x for x in range(3,2000001,2) if isPrime(x)]
print(sum(primes))
