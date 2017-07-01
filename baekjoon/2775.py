def GetNum_timeout(k,n):
    if k == 0:
        return n
    result = 0
    for i in range(0,n+1):
        result += GetNum(k-1, i)
    return result

apt = []

def makeApt(k,n):
    apt.append([])
    for i in range(n):
        apt[0].append(i+1)

    for i in range(k-1):
        apt.append([])

        for j in range(n):
            res = 0
            for k in range(j+1):
                res += apt[i][k]
            apt[i+1].append(res)

def GetNum(k,n):
    result = 0

    for i in range(n):
        result += apt[k-1][i]

    return result

if __name__ == "__main__":
    num = int(input())
    K, N = [], []
    for _ in range(num):
        K.append(int(input()))
        N.append(int(input()))

    makeApt(max(K), max(N))

    

    for i in range(num):
        print(GetNum(K[i],N[i]))

# 1호 : 1
# 2호 : 2,3,4,5,6 : k
# 3호 : 3, 6, 10, 15 : n + (n+1) + (n+2) ... kn+ 0~n까지 합
# 4호 : 4, 10, 20, 35 : 6, 10, 15
