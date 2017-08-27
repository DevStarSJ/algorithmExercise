import functional as F
import copy

class BadNeighbors:
    max_acc = 0
    patterns = {}

    def max_donations(self, donations):
        num_neighbors = len(donations)
        enables = [1 for _ in range(num_neighbors)]
        self.max_acc = 0

        self.donate_step(copy.deepcopy(enables), donations, 0, num_neighbors)

        return self.max_acc

    def enable_donate(self, selected, enables, num_neighbors):
        e1 = copy.deepcopy(enables)
        e1[selected] = 0
        e1[(selected + 1) % num_neighbors] = 0
        e1[(selected - 1) % num_neighbors] = 0
        return e1

    def donate_step(self, enables, donations, accumulation, num_neighbors):
        enables_pattern = ''.join([str(i) for i in enables])
        if enables_pattern in self.patterns.keys():
            if self.patterns[enables_pattern] < accumulation:
                self.patterns[enables_pattern] = accumulation
            else:
                return
        else:
            self.patterns[enables_pattern] = accumulation

        if F.all(enables, F.is_false):
            if accumulation > self.max_acc:
                self.max_acc = accumulation

        e1 = copy.deepcopy(enables)

        for i, e in enumerate(e1):
            if not e:
                continue

            new_acc = donations[i] + accumulation
            e2 = self.enable_donate(i, e1, num_neighbors)
            self.donate_step(e2, donations, new_acc, num_neighbors)


B = BadNeighbors()
print(B.max_donations([10,3,2,5,7,8]))
print(B.max_donations([11,15]))
print(B.max_donations([7,7,7,7,7,7,7]))
print(B.max_donations([1,2,3,4,5,1,2,3,4,5]))
print(B.max_donations([94,40,49,65,21,21,106,80,92,81,679,4,61,6,237,12,72,74,29,95,265,35,47,1,61,397,52,72,37,51,1,81,45,435,7,36,57,86,81,72]))
