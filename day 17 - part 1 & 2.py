from collections import deque

def hor(start):
    h = [start]
    x, y = start

    while (x-1, y+1) in grid and grid[(x-1,y+1)] in '#~|' and ((x-1,y) not in grid or grid[(x-1,y)] == '|'):
        h.append((x-1, y))
        x -= 1
    if (x-1,y) not in grid and (x,y+1) in grid and grid[(x,y+1)] in '#~|':
        h.append((x-1,y))
    x, y = start
    
    while (x+1, y+1) in grid and grid[(x+1,y+1)] in '#~|' and ((x+1,y) not in grid or grid[(x+1,y)] == '|'):
        h.append((x+1, y))
        x += 1
    if (x+1,y) not in grid and (x,y+1) in grid and grid[(x,y+1)] in '#~|':
        h.append((x+1, y))

    flow = [z for z in h if (z[0], z[1] + 1) not in grid]
    if flow:
        for z in flow:
            if z not in v_seen:
                v_queue.append(z)
        for z in h:
            grid[z] = '|'
    else:
        for z in h:
            grid[z] = '~'
            h_seen.add(z)
        x, y = start
        if (x, y-1) not in h_seen:
            h_queue.append((x, y-1))
        
    
def vert(mx):
    x,y = v_queue.popleft()
    v_seen.add((x,y))
    while (x, y + 1) not in grid and y < mx:
        grid[(x, y + 1)] = '|'
        x, y = (x, y + 1)
    if not y >= mx and grid[(x, y + 1)] not in '|':
        if (x,y) not in h_seen:
            h_queue.append((x,y))
    

with open("2018day17.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    grid = {}
    for row in data:
        static, rng = sorted(row.split(', '), key = lambda x: len(x))
        s_rng = [int(static.split('=')[1])]
        r = [int(x) for x in rng.split('=')[1].split('..')]
        r_rng = [x for x in range(r[0], r[1]+1)]
        if 'x' in static:
            grid.update({(x,y) : '#' for x in s_rng for y in r_rng})
        else:
            grid.update({(x,y) : '#' for x in r_rng for y in s_rng})
    mx = max(k[1] for k in grid.keys())
    mn = min(k[1] for k in grid.keys())
    current = (500, 0)
    v_queue = deque([current])
    h_queue = deque([])
    v_seen = set([current])
    h_seen = set([])
    while v_queue or h_queue:
        if v_queue:
            vert(mx)
        while h_queue:
            hor(h_queue.popleft())
    print(len([v for k,v in grid.items() if v in '~|' and k[1] >= mn]))
    print(len([v for k,v in grid.items() if v in '~']))
