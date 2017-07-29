class NumberMagicEasy:
    taros_card = [
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,9,10,11,12],
        [1,2,5,6,9,10,13,14],
        [1,3,5,7,9,11,13,15]
    ]

    def the_number(self, answer):
        all_answer = [x for x in range(1, 17)]
        for i, a in enumerate(answer):
            go = self.yes if a == 'Y' else self.no
            go(all_answer, self.taros_card[i])

        return all_answer[0]

    def yes(self, all_answer, card):
        numbers = [x for x in range(1,17) if not x in card]
        for x in numbers:
            if x in all_answer:
                all_answer.remove(x)

    def no(self, all_answer, card):
        numbers = [x for x in range(1,17) if x in card]
        for x in numbers:
            if x in all_answer:
                all_answer.remove(x)

taro = NumberMagicEasy()

print(taro.the_number('YNYY'))
print(taro.the_number('YNNN'))
print(taro.the_number('NNNN'))
print(taro.the_number('YYYY'))
print(taro.the_number('NYNY'))