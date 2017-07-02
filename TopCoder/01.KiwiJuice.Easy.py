def thePouring(capacities, bottles, fromId, toId):
    for f, t in zip(fromId, toId):
        qty = min(capacities[t] - bottles[t], bottles[f])
        bottles[f] -= qty;
        bottles[t] += qty;
    return bottles

print(thePouring([20,20],[5,8],[0],[1]))
print(thePouring([30,20,10],[10,5,5],[0,1,2],[1,2,0]))
print(thePouring([14, 35, 86, 58, 25, 62],[6, 34, 27, 38, 9, 60],[1, 2, 4, 5, 3, 3, 1, 0],[0, 1, 2, 4, 2, 5, 3, 1]))
print(thePouring([700000, 800000, 900000, 1000000],[478478, 478478, 478478, 478478],[2, 3, 2, 0, 1],[0, 1, 1, 3, 2]))