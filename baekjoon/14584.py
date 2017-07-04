input_str = str(input())
num_words = int(input())
words = []
for _ in range(num_words):
    words.append(str(input()))


def shift_sentence(sentence, num_shift):
    asciis = [ord(x) + num_shift for x in sentence]
    asciis = map(lambda x: x if x <= 122 else x-26, asciis)
    new_sentence = ''.join([chr(x) for x in asciis])
    return new_sentence

def find_sentence(s1):
    for i in range(26):
        sentence = shift_sentence(s1,i)
        #print(i,sentence)
        for w in words:
            if w in sentence:
                #print("FIND")
                print(sentence)
                return

find_sentence(input_str)
