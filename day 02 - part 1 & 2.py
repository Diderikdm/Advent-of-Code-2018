with open("2018day2.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    print(sum(1 for x in data if any(x.count(y) == 2 for y in x)) * sum(1 for x in data if any(x.count(y) == 3 for y in x)))
    sort = sorted(data, key = lambda x : -max(sum(int(x[e] == y[e]) for e in range(len(x))) for y in data if x != y))
    print(''.join([x for e,x in enumerate(sort[0]) if sort[1][e] == x]))
