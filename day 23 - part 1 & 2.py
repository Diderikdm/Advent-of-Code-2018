with open("2018day23.txt", 'r') as file:
    data = [x.split('>, r=') for x in file.read().splitlines()]
    data = {tuple([int(x) for x in y[0].split('<')[1].split(',')]) : int(y[1]) for y in data}
    mx = max(data.items(), key = lambda x: x[1])
    print(len([k for k in data.keys() if abs(k[0] - mx[0][0]) + abs(k[1] - mx[0][1]) + abs(k[2] - mx[0][2]) <= mx[1]]))
    manhattan = {k : sum([abs(x) for x in k]) for k in data.keys()}
    minmax = sorted([(manhattan[k] - data[k], 1) for k in data.keys()] + [(manhattan[k] + data[k] + 1, -1) for k in data.keys()], key = lambda x: x[0])
    x, mx = 0, 0
    while minmax:
        manhattan, prio = minmax.pop(0)
        x += prio
        if x > mx:
            best = manhattan
            mx = x
    print(best)
