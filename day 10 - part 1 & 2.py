from itertools import combinations
from collections import defaultdict

with open("2018day10.txt", 'r') as file:
    data = [[(int(y[0]), int(y[1])) for y in [b.split('>')[0].split(',') for b in a]] for a in [x.split('<')[1:] for x in file.read().splitlines()]]
    grid = {e: {x[0] : x[1]} for e,x in enumerate(data)}
    adj = lambda x,y : list(set([(x+a,y+b) for a,b in list(combinations([-1,0,1]*2, 2)) if (a,b) != (0,0) and (x+a, y+b) in [next(iter(v.keys())) for k,v in grid.items()]]))
    temp = defaultdict(dict)
    i = 0 
    while not all([adj(*next(iter(v.keys()))) for k,v in grid.items()]):
        for e,f in grid.items():
            for k,v in f.items():
                amp = 1
                if k[0] // -v[0] > 1000:
                    amp = 10000
                temp[e][(k[0] + v[0] * amp, k[1] + v[1] * amp)] = v
        grid = {k:v for k,v in temp.items()}
        temp = defaultdict(dict)
        i += amp
    min_x, max_x = min(next(iter(v.keys()))[0] for k,v in grid.items()), max(next(iter(v.keys()))[0] for k,v in grid.items())
    min_y, max_y = min(next(iter(v.keys()))[1] for k,v in grid.items()), max(next(iter(v.keys()))[1] for k,v in grid.items())
    img = ''
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            img += '#' if (x,y) in [next(iter(v.keys())) for k,v in grid.items()] else '.'
        img += '\n'
    print(img)
    print(i)
