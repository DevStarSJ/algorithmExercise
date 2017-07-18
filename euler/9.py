#a + b + c = 1000 인 피타고라스 수(a**2 + b**2 = c**2) a, b, c는 한 가지 뿐입니다. 이 때, a × b × c

def maxPythagorean(num):
    for i in range(1,num-5):
        for j in range(i+1, num-5-i):
            k = num - i - j
            if not i < j < k:
                continue
            if i*i + j*j == k*k:
                return [i,j,k]

import functools
print(functools.reduce(lambda x,y:x*y, maxPythagorean(1000)))