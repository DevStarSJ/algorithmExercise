#inList = [1, 5, 3, 3, 7];

inList = [1, 3, 5, 3, 4];

def isSortedSwap(nums):
    numSorted = sorted(nums)
    #print(numSorted)

    diffNum = 0
    for i in range(0,len(nums)):
        if nums[i] != numSorted[i]:
            #print(nums[i],numSorted[i])
            diffNum += 1
            if diffNum > 2:
                return False

    #print(diffNum)
    if diffNum == 1:
        return False

    return True

print(isSortedSwap(inList))
