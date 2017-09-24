import math

def count_roads(roads):
    len_roads = len(roads)
    essential_raods = []
    essential_group = []

    for i, line in enumerate(roads):
        for j, point in enumerate(line):
            if point == "Y":
                road = (i, j) if j > i else (j, i)
                if road not in essential_raods:
                    essential_raods.append(road)



    for i, road in enumerate(essential_raods):
        # 한 점에서 필수 도로가 3개 이상인게 있으면 가능한 경우의 수가 없음
        c = 0
        if i < len(essential_raods) - 1:
            for j in range(i, len(essential_raods)):
                r2 = essential_raods[j]
                if road[0] == r2[0] and road[1] == r2[1]: continue
                if road[0] in r2 or road[1] in r2: c += 1
        if c > 1:
            return 0

        # 순환이 되어 있으면 가능한 경우의 수가 없음
        traveled = [road[0], road[1]]
        start = road[0]
        current = road[1]
        is_change = True
        while is_change:
            is_change = False
            for r2 in essential_raods:
                if (r2[0] in traveled) and (r2[1] in traveled):
                    continue
                if current in r2:
                    current = r2[1] if r2[0] == current else r2[0]
                    traveled.append(current)
                    is_change = True
                    break
            if start == current:
                return 0

        if traveled not in essential_group and traveled[::-1] not in essential_group:
            essential_group.append(traveled)

    len_roads -= len(essential_raods)
    result = len_roads
    for i in range(2, len_roads):
        result *= i
    return result * int(math.pow(2, len(essential_group)))


print(count_roads(["NYN","YNN","NNN"]))
print(count_roads(["NYYY","YNNN","YNNN","YNNN"]))
print(count_roads(["NY","YNY","YYN"]))
print(count_roads(["NNNNNY","NNNNYN","NNNNYN","NNNNNN","NYYNNN","YNNNNN"]))
