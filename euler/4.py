#세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수(palindrome: 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수)

def isPalindrome(num):
    s = str(num)
    start = 0
    end = len(s) - 1
    return s == s[::-1]

maxPalindrome = 0

for i in range(999,111,-1):
    for j in range(999,111,-1):
        k = i * j
        if maxPalindrome != 0 and k < maxPalindrome:
            break
        if isPalindrome(k):
            maxPalindrome = max(maxPalindrome, k)
            break;

print(maxPalindrome)