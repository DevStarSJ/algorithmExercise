def printSeq(s):
    print(" ".join(s))

def isSorted(s):
    l = len(s)
    for i in range(0,l-1):
        if seq[i] > seq[i+1]:
            return False
    return True

def do(s):
    l = len(s)
    for i in range(0,l-1):
        if s[i] > s[i+1]:
            s[i], s[i+1] = s[i+1], s[i]
            printSeq(s)

if __name__ == "__main__":
    seq = input().split()
    while not isSorted(seq):
        do(seq)