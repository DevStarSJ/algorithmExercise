class HandShaking:
    def count_perfect(self, n):
        if n % 2 > 0:
            return None

        shaking_case = [1, 2]

        if n < 6:
            return shaking_case[n//2-1]

        for i in range(6, n+1, 2):
            case_total = 0

            for j in range(1, i, 2):
                left = j - 1
                right = i - j - 1
                case_step_left = shaking_case[(left-1) // 2] if left > 0 else 1
                case_step_right = shaking_case[(right-1) // 2] if right > 0 else 1
                case_total += case_step_left * case_step_right

            shaking_case.append(case_total)

        return shaking_case[(n-1)//2]

H = HandShaking()
print(H.count_perfect(2))
print(H.count_perfect(4))
print(H.count_perfect(6))
print(H.count_perfect(8))
print(H.count_perfect(10))
print(H.count_perfect(20))
