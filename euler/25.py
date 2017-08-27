fibonacci = [1,1]

while True:
    v = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(v)
    if len(str(v)) == 1000:
        print(len(fibonacci))
        break