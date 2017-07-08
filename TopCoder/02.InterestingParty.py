def best_invitation(first, second):
    interestings = set(first + second)
    countings = {}
    for interest in interestings:
        countings[interest] = 0
        for i in range(len(first)):
            if first[i] == interest or second[i] == interest:
                countings[interest] += 1
    most_key = max(countings, key=lambda x: countings[x])
    return countings[most_key]

print(best_invitation(["fishing", "gardening", "swimming", "fishing"],
                      ["hunting", "fishing", "fishing", "biting"]))

print(best_invitation(["variety", "diversity", "loquacity", "cortesy"],
                      ["talking", "speaking", "discussion", "metting"]))

print(best_invitation(["snakes", "programming", "cobra", "monty"],
                      ["python", "python", "anaconda", "python"]))

print(best_invitation(list("topcodersingleroundmatchfourni"),
                      list("nefourjanuarytwentytwosaturday")))