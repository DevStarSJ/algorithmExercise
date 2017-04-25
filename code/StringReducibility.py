inStr = "ABBCCBBBBAAAAACCCCBBBAAACCAABBCCC"

ruleSet = {"AB":"AA", "BA":"AA", "CB":"CC", "BC":"CC", "AA":"A", "CC":"C"};
keySet = ruleSet.keys()

def applyRule(s):

    isChanged = True

    while isChanged is True:
        isChanged = False
        i = 0
        length = len(s)

        while i <= length - 2:
            sHead = s[:i] if i > 0 else ""
            sRest = s[i:]
            token = sRest[:2]

            if token in keySet:
                s = sHead + sRest.replace(token, ruleSet[token], 1)
                i += 2
                isChanged = True
            else:
                i += 1
    return s

a = applyRule(inStr)
print(a)

