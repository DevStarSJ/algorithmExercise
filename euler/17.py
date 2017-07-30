#one, two, three, four, five, six, seven, eight, nine
# ten, eleven, twenve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
one_count = [0,3,3,5,4,4,3,5,5,4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]

#ten, twenty, thiry, fourty, fifty, sixty, seventy, eighty, ninety
ten_count = [0,3,6,5,6,5,5,7,6,6]

AND = 3
HUNDRED = 7
THOUSAND = 8

total = one_count[1] + THOUSAND

for i in range(1, 1000):
    word_len = 0
    tens = i % 100
    if tens < 20:
        word_len = one_count[tens]
    else:
        one = i % 10
        ten = (i // 10 % 10)
        word_len = one_count[one] + ten_count[ten]
    hundred = (i // 100) % 10
    if hundred > 0:
        if word_len > 0:
            word_len += AND
        word_len += one_count[hundred] + HUNDRED
    total += word_len

print(total)
