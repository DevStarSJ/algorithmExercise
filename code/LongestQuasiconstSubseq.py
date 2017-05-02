def LongestQuasiconstSubseq(seq):

    uniqueSeq = sorted(list(set(seq)))

    cnt = len(uniqueSeq)

    maxQuasi = 0

    for i, v in enumerate(uniqueSeq):
        for j in range(i,cnt):
            w = uniqueSeq[j]
            if abs(w - v) <= 1:
                maxQuasi = max(maxQuasi,len([ e for e in seq if v <= e <= w ]))
            else:
                break

    return maxQuasi
            
print(LongestQuasiconstSubseq([6, 10, 6, 9, 7, 8]))
print(LongestQuasiconstSubseq([6, 10, 1, 2, 6, 6, 7]))
print(LongestQuasiconstSubseq([5, 5, 3, 3, 9]))
print(LongestQuasiconstSubseq([5, 6, 1, 3, 2, 4]))
print(LongestQuasiconstSubseq([6, 10, 6, 9, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8 ]))
print(LongestQuasiconstSubseq([1,1,1,1,1,1,1 ]))
print(LongestQuasiconstSubseq([-1,-1,-1,-1,-2,0,1,-1,0,1,0]))
print(LongestQuasiconstSubseq([6,10,6,9,7,8,7,6,10,1,1,1,1]))

