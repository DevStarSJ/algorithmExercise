class BadNeighbors:
    max_acc = 0
    patterns = {}

    def max_donations(self, donations):
        num_neighbors = len(donations)
        return max(self.dynamic_step(0, num_neighbors - 1, donations),
                   self.dynamic_step(1, num_neighbors, donations))

    def dynamic_step(self, start, end, donations):
        num_neighbors = len(donations)
        max_donate_list = [0 for _ in range(num_neighbors)]

        for i in range(start, end):
            if i < 2:
                max_donate_list[i] = donations[i]
            elif i == 2:
                max_donate_list[i] = donations[i] + max_donate_list[0]
            else:
                max_before_2 = max(max_donate_list[i-2], max_donate_list[i-3])
                max_donate_list[i] = donations[i] + max_before_2

        return max(max_donate_list)

B = BadNeighbors()
print(B.max_donations([10,3,2,5,7,8]))
print(B.max_donations([11,15]))
print(B.max_donations([7,7,7,7,7,7,7]))
print(B.max_donations([1,2,3,4,5,1,2,3,4,5]))
print(B.max_donations([94,40,49,65,21,21,106,80,92,81,679,4,61,6,237,12,72,74,29,95,265,35,47,1,61,397,52,72,37,51,1,81,45,435,7,36,57,86,81,72]))
