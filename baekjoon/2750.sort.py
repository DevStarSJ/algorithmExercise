def bubbleSort(seq):
    num = len(seq)
    num2 = num - 1
    for i in range(0, num -1):
        for j in range(0, num2):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
        num2 -= 1

    return seq

def selectionSort(seq):
    num = len(seq)
    leftMin = 0

    for i in range(0, num):
        leftMin = i
        for j in range(i+1, num):
            if seq[leftMin] > seq[j]:
                leftMin = j
        seq[i], seq[leftMin] = seq[leftMin], seq[i]

    return seq

def intertionSort(seq):
    num = len(seq)

    for i in range(1, num):
        for j in range(i, 0, -1):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]
            else:
                break
    return seq
            

if __name__ == "__main__":
    num = int(input())
    seq = []
    for i in range(0, num):
        seq.append(int(input()))

    for i in intertionSort(seq):
        print(i)
