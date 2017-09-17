import mathExt as M
import functional as F

def get_except(a, b):
    return [aa for aa in a if not F.any(b, lambda bb: bb in aa)]

digits = list(range(1,10))
set_digits = set(digits)

sets = [[]] + [ M.powerset_check_length(digits, 1, x) for x in range(1, 8)]

set_a = sets[7]

results = set()

for a in set_a:
    len_a = len(a)
    for num_b in range(1, 9 - len(a)):
        set_b = get_except(sets[num_b], a)
        for b in set_b:
            len_b = len(b)
            len_c = 9 - len_a - len_b

            if not (len_c <= len_a + len_b <= len_c + 1):
                continue

            c = list((set_digits - set(a+b)))

            for cm in M.combination(c):
                cc = int("".join(F.map(cm, str)))
                if cc in results:
                    continue

                for am in M.combination(a):
                    for bm in M.combination(b):
                        aa = int("".join(F.map(am, str)))
                        bb = int("".join(F.map(bm,str)))

                        if aa * bb == cc:
                            print(aa, "x", bb,"=",cc)
                            results.add(cc)
results = list(results)
print(sum(results), ":", results)
