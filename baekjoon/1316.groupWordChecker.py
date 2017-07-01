def isGroupWord(word):
    #word = word.lower()
    letter = []
    for i, w in enumerate(word):
        if w in letter:
            if word[i-1] == w:
                continue
            return False
        else:
            letter.append(w)
    return True


if __name__ == "__main__":
    num = int(input())
    words = []
    for _ in range(num):
        words.append(input())
    
    result = 0
    for w in words:
        if isGroupWord(w):
            result += 1
    print(result)