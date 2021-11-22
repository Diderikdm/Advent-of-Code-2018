def find_routes(start, target, steps, best):
    q = [(steps, start[0], start[1], 1)]
    while q:
        q = sorted(q, key = lambda x: x[0])
        steps, x, y, tool = q.pop(0)
        if (x,y,tool) in best and best[(x,y,tool)] <= steps:
            continue
        best[(x,y,tool)] = min(best[(x,y,tool)] if (x,y,tool) in best else steps, steps)
        for a, b in ((x,y+1), (x-1,y), (x+1,y), (x,y-1)):
            if (a,b) in grid:
                if grid[(a,b)] in tools[tool]:
                    q.append((steps + 1, a, b, tool))
                else:
                    for z in [w for w in [0,1,2] if w != tool and grid[(x,y)] in tools[w]]:
                        q.append((steps + 7, a, b, z))               
    return best[(target[0], target[1], 1)] - 7 + 1


def calculate_type(current, depth):
    x,y = current
    if current in [(0,0), target]:
        geoi[current] = 0
    elif y == 0:
        geoi[current] = x * 16807
    elif x == 0:
        geoi[current] = y * 48271
    else:
        geoi[current] = erol[(x-1,y)] * erol[(x,y-1)]
    erol[current] = (geoi[current] + depth) % 20183
    return erol[current] % 3
            

with open("2018day22.txt", 'r') as file:
    data = [x.split()[1] for x in file.read().splitlines()]
    depth = int(data[0])
    target = tuple([int(x) for x in data[1].split(',')])
    grid = {}
    geoi = {}
    erol = {}
    for y in range(target[1] * 2):
        for x in range(target[0] * 2):
            grid[(x,y)] = calculate_type((x,y), depth)
    print(sum([v for k,v in grid.items() if k[0] <= target[0] and k[1] <= target[1]]))
    current = (0,0)
    bests = {}
    tools = {0 : [1,2], 1 : [0,2], 2 : [0,1]}
    print(find_routes((0,0), target, 0, {}))

