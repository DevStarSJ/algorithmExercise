class CrazyBot:

    total_prob = 0.0
    probs = {}
    depth = 0
    directions = []
    passed_point = []

    def go(self, step, path, prob):
        #print(step, path, self.total_prob, self.passed_point)
        if not path == '':
            next_point = self.is_valid_path(path)
            if next_point is False:
                return
            else:
                self.passed_point.append(next_point)

        if step >= self.depth:
            self.total_prob += prob
            #print("BINGO", step, self.total_prob,self.passed_point)
            self.passed_point.pop()

            return

        for d in self.directions:
            self.go(step+1, d, prob * self.probs[d])

        self.passed_point.pop()

    def is_valid_path(self, d):
        current_point = self.passed_point[-1]

        direction = [0 if d in ['N', 'S'] else (1 if d == 'E' else -1),
                     0 if d in ['E', 'W'] else (1 if d == 'N' else -1)]
        next_point = (current_point[0] + direction[0],
                      current_point[1] + direction[1])
        if next_point in self.passed_point:
            return False
        else:
            return next_point

    def get_probability(self, n, east, west, south, north):
        self.total_prob = 0.0
        self.probs = {'N': north*0.01, 'S': south * 0.01, 'E': east * 0.01, 'W': west * 0.01}
        self.directions = [k for k in self.probs.keys() if self.probs[k] > 0]
        self.depth = n
        self.passed_point = [(0,0)]

        self.go(0, '', 1)

        return self.total_prob


crazy_bot = CrazyBot()

print(crazy_bot.get_probability(1, 25, 25, 25, 25))
print(crazy_bot.get_probability(2, 25, 25, 25, 25))
print(crazy_bot.get_probability(7, 50, 0, 0, 50))
print(crazy_bot.get_probability(14, 50, 50, 0, 0))
print(crazy_bot.get_probability(14, 25, 25, 25, 25))




