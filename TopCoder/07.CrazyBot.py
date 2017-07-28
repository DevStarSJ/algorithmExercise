import functional as F

def is_valid_path(path):
    passed_point = [(0,0)]
    current_point = (0,0)

    for p in path:
        direction = [0 if p in ['N', 'S'] else (1 if p == 'E' else -1),
                     0 if p in ['E', 'W'] else (1 if p == 'N' else -1)]
        next_point = (current_point[0] + direction[0],
                      current_point[1] + direction[1])
        if next_point in passed_point:
            return False
        else:
            passed_point.append(next_point)
            current_point = next_point
    return True


def calc_probability(path, east, west, sourth, north):
    dict_prob = {'N': north*0.01, 'S': sourth * 0.01, 'E': east * 0.01, 'W': west * 0.01}
    result = 1
    for p in path:
        result *= dict_prob[p]
    return result


class CrazyBot:
    def get_probability(self, n, east, west, south, north):
        paths = ['']

        for i in range(n):
            new_path = []
            #print(paths)
            for p in paths:
                if east > 0:
                    new_p = p + 'E'
                    if is_valid_path(new_p):
                        new_path.append(new_p)
                if west > 0:
                    new_p = p + 'W'
                    if is_valid_path(new_p):
                        new_path.append(new_p)
                if south > 0:
                    new_p = p + 'S'
                    if is_valid_path(new_p):
                        new_path.append(new_p)
                if north > 0:
                    new_p = p + 'N'
                    if is_valid_path(new_p):
                        new_path.append(new_p)
            paths = new_path
            #print("i, new_path",i, len(new_path))

        return F.go(paths,
                    F.curryr(F.map)(lambda x: calc_probability(x, east, west, south, north)),
                    F.sum)


crazy_bot = CrazyBot()

print(crazy_bot.get_probability(1, 25, 25, 25, 25))
print(crazy_bot.get_probability(2, 25, 25, 25, 25))
print(crazy_bot.get_probability(7, 50, 0, 0, 50))
print(crazy_bot.get_probability(14, 50, 50, 0, 0))
print(crazy_bot.get_probability(14, 25, 25, 25, 25))




