# 1000보다 작은 자연수 중 3 or 5의 배수들의 합
print(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))
