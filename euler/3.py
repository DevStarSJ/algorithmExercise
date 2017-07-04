#600851475143의 소인수 중 가장 큰수
import math

def isPrime(num):
    if num == 2 or num == 3: return True
    if num % 2 == 0 or num % 3 == 0: return False

    for i in range(3,int(math.sqrt(num))+1,2):
        if num % i == 0: return False
    return True

def getPrimeFactorization(num):
    acc = num
    primes = []
    index = 2
    while index <= acc:
        if isPrime(index) and acc % index == 0:
            primes.append(index)
            acc /= index
        index += 1
    return primes

primes = getPrimeFactorization(600851475143)
print(max(primes))