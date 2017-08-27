case_lexicographic = [1]

for i in range(2, 11):
    case_lexicographic.append(i * case_lexicographic[i-2])

def get_case_lexicographic(n, m):
    nums = sorted([i for i in range(m)])
    num_sequence = [0 for _ in range(m)]
    rest = n - 1

    for num_subset in range(m, 0, -1):
        case = case_lexicographic[num_subset - 2]
        div = rest // case
        rest = rest % case
        num_sequence[m - num_subset] = div
    num_sequence[m-1] = rest
    print(num_sequence)

    seq = ""
    for num_subset in num_sequence:
        print(nums)
        v = nums[num_subset]
        seq += str(v)
        nums.remove(v)
        nums.sort()

    return seq

print(get_case_lexicographic(1000000, 10))

