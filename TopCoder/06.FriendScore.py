class FriendScore:
    def highestScores(self, friends):
        num = len(friends)
        first_step = [set() for _ in range(num)]
        for i, line in enumerate(friends):
            for j, v in enumerate(line):
                if v == 'Y':
                    first_step[i].add(j)

        best_score = 0
        second_step = [set() for _ in range(num)]
        for i, single in enumerate(first_step):
            second_step[i].update(list(single))
            for friend in single:
                second_step[i].update(list(first_step[friend]))
            if (i in list(second_step[i])):
                second_step[i].remove(i)
            score = len(second_step[i])

            if score > best_score:
                best_score = score

        return best_score

fs = FriendScore()
print(fs.highestScores(['NNN','NNN','NNN']))
print(fs.highestScores(['NYY','YNY','YYN']))
print(fs.highestScores(['NYNNN','YNYNN','NYNYN', 'NNYNY','NNNYN']))

