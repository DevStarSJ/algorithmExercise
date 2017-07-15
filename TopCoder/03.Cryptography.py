import functional as F

def encrypt(numbers):
    min_number = min(numbers)
    return int(F.reduce(numbers, lambda a,b: a*b, 1) / min_number * (min_number +1))

print(encrypt([1,2,3]))
print(encrypt([1,3,2,1,1,3]))
print(encrypt([1000,999,998,997,996,995]))
print(encrypt([1,1,1,1]))
