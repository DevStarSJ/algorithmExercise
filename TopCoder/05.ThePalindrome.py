def is_palindrome(sentence):
    list_sen = list(sentence)
    return list_sen == list_sen[::-1]

def find_first_cursor(sentence):
    for i in range(1, len(sentence)):
        if is_palindrome(sentence[i:]):
            return i - 1

def find_shortest_palindrome(sentence):
    length = len(sentence)
    if length < 2: return length
    cursor = find_first_cursor(sentence)

    while cursor >= 0:
        if not is_palindrome(sentence):
            sentence += sentence[cursor]
            cursor -= 1
        else: break

    return len(sentence)

print(find_shortest_palindrome("abab"))
print(find_shortest_palindrome("abacaba"))
print(find_shortest_palindrome("qwerty"))
print(find_shortest_palindrome("abdfhdyrbdbsdfghjkllkjhgfds"))


