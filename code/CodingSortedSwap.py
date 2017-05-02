#inList = [1, 5, 3, 3, 7];

inList = [1, 3, 5, 3, 4];

def isSorted(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] > nums[i+1]:
            return False
    return True

def isSortedSwap(nums):
    if isSorted(nums):
        return True
    inLength = len(inList)
    #print(inLength)
    for i in range(0, inLength):
        for j in range(i+1, inLength):
            if nums[i] != nums[j] and nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                #print(nums)
                if isSorted(inList):
                    return True
                else:
                    nums[i], nums[j] = nums[j], nums[i]
    return False

print(isSortedSwap(inList))

