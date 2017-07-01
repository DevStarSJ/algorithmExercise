#피보나치 수열 짝수이면서 4백만 이하인 모든 항의 합

sum = 0
fibonacci1 = 1
fibonacci2 = 2
while fibonacci2 <= 4000000:
    if fibonacci2 % 2 == 0:
        sum += fibonacci2
    fibonacci1, fibonacci2 = fibonacci2, fibonacci1 + fibonacci2
print(sum)