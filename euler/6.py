#그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이
print(sum([x for x in range(1,101)])**2 - sum([x*x for x in range(1,101)]))