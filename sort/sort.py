def bubbleSort(seq):
    num = len(seq)
    num2 = num - 1
    for i in range(num -1):
        for j in range(num2):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
        num2 -= 1

    return seq

def selectionSort(seq):
    num = len(seq)
    leftMin = 0

    for i in range(num):
        leftMin = i
        for j in range(i+1, num):
            if seq[leftMin] > seq[j]:
                leftMin = j
        seq[i], seq[leftMin] = seq[leftMin], seq[i]

    return seq

def insert_sort(seq):
    num = len(seq)

    for i in range(1, num):
        for j in range(i, 0, -1):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]
            else:
                break
    return seq

def compare_two(seq):
    num = len(seq)
    if num <= 1:
            return seq
    elif num == 2:
        if seq[0] > seq[1]:
            seq[0], seq[1] = seq[1], seq[0]
        return seq   

def quickSort(seq):
    print(seq)
    num = len(seq)

    if num <= 2:
        return compare_two(seq)

    p = int(num / 2)
    pivot = seq[p]

    print("pivot : ",pivot, p)

    smaller = [i for i in seq if i < pivot]
    bigger = [i for i in seq if i > pivot]
    same = [i for i in seq if i == pivot]

    print("smaller = ", smaller)
    print("bigger = ", bigger)

    return quickSort(smaller) + same  + quickSort(bigger)

def quickSort2(seq):
    print("input : ",seq)
    num = len(seq)

    if num <= 2:
        return compare_two(seq)

    p = num - 1
    pivot =seq[p]

    print("pivot : ",pivot, p)

    i = 0
    j = num - 2
    while i < j:
        if seq[i] > pivot and seq[j] <= pivot:
            seq[i], seq[j] = seq[j], seq[i]
            i += 1
            j -= 1
        else:
            if seq[i] <= pivot:
                i += 1
            if seq[j] > pivot:
                j -= 1

    seq[i], seq[p] = seq[p], seq[i]

    print("after : ",seq)
    return quickSort2(seq[:i]) + quickSort2(seq[i:])

def mergeSort(seq):
    print("input : " ,seq)
    num = len(seq)

    if num <= 2:
        return compare_two(seq)
    
    pivot = num // 2

    seq1, seq2 = mergeSort(seq[:pivot]), mergeSort(seq[pivot:])
    print(seq1, seq2)
    len1, len2 = len(seq1), len(seq2)
    a,b = 0, 0

    result = []

    while a != len1 or b != len2:
        if a != len1 and (b == len2 or seq1[a] < seq2[b]):
            result.append(seq1[a])
            a += 1
        else:
            result.append(seq2[b])
            b += 1
    return result

if __name__ == "__main__":
    #num = int(input())
    #seq = []
    #num = 10
    seq = [3 ,5 ,2 ,7 ,4 ,6 ,2 ,9 ,4 ,1, 13, 45, 12, 0, 1, 5, 6, 3, 4]
    # for i in range(0, num):
    #     seq.append(int(input()))

    for i in insert_sort(seq):
        print(i)
