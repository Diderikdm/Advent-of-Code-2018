with open("2018day6.txt", 'r') as file:
    data = [(int(x), int(y)) for x,y in [z.split(', ') for z in file.read().splitlines()]]
    bests = {x : [] for x in data}
    min_x, max_x, min_y, max_y = min(x[0] for x in data), max(x[0] for x in data), min(x[1] for x in data), max(x[1] for x in data)
    center = ((max_x - min_x) / 2, (max_y - min_y) / 2)
    edges = set()
    for x in data:
        offset_x, offset_y = x[0] - center[0], x[1] - center[1]
        edges.add(max(data, key = lambda x: abs(offset_x * 1000000 + x[0]) + abs(offset_y * 1000000 + x[1])))
    valids = 0
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y):
            if sum(abs(z[0] - x) + abs(z[1] - y) for z in data) < 10000:
                valids += 1
            lst = sorted(data, key = lambda z: abs(z[0] - x) + abs(z[1] - y))
            if abs(x - lst[1][0]) + abs(y - lst[1][1]) != abs(x - lst[0][0]) + abs(y - lst[0][1]) and lst[0] not in edges:
                bests[lst[0]].append((x,y))
    print(len(max(bests.values(), key = lambda x: len(x))))
    print(valids)
