import functional as F
names = sorted(F.map(open("names.txt", 'r').readline().split(','),
              lambda x: x.replace('"','')))
A = ord('A')
def getValue(c):
    return ord(c) - A + 1

score = 0
for i, name in enumerate(names):
    score += (i+1) * sum([getValue(c) for c in name])

print(score)

