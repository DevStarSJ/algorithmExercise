def batch_system(duration, user):
    user_time = {}
    for i, v in enumerate(zip(user, duration)):
        u, d = v
        if v[0] not in user_time:
            user_time[u] = (0, [])
        user_time[u] = (user_time[u][0] + d, sorted(user_time[u][1] + [i]))

    times = sorted(list(user_time.values()), key= lambda x: (x[0], x[1]))
    result = []

    for _, indexs in times:
        result += indexs

    return result


print(batch_system([400,100,100,100], ["D", "S", "S", "M"]))
print(batch_system([200,200,200], ["G", "S", "W"]))
print(batch_system([100,200,50], ["H", "H", "Y"]))



