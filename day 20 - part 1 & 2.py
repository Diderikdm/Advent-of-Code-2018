from collections import deque

def find_routes(grid, start, paths = {}):
    q = deque([[start]])
    prev = set([start])
    while q:
        path = q.popleft()
        x,y = path[-1]
        if (x,y) not in paths:
            paths[(x,y)] = path[:]
        for a, b in ((x,y-1), (x-1,y), (x+1,y), (x,y+1)):
            if grid[(a,b)] != '#' and (a,b) not in prev:
                q.append(path + [(a,b)])
                prev.add((a,b))
    return paths


def fill_neighbors(current):
    x,y = current
    for a,b in ((x+1,y+1), (x-1,y-1), (x-1,y+1), (x+1,y-1)):
        grid[(a,b)] = '#'
    for a,b in ((x,y+1), (x,y-1), (x-1,y), (x+1,y)):
        if (a,b) not in grid:
            grid[(a,b)] = '?'


def walk(data, current, i):
    backup = current
    while i < len(data):
        if data[i] == '(':
            i = walk(data, current, i+1)
            continue
        if data[i] == '|':
            current = backup
            i += 1
            continue
        if data[i] == ')':
            i += 1
            return i
        door, door_coord, nxt = dirs[data[i]](*current)
        grid[door_coord] = door
        current = nxt
        grid[current] = '.'
        fill_neighbors(current)
        i += 1

        
with open("2018 day20.txt", 'r') as file:
    data = file.read()[1:-1]
    current = (0,0)
    grid = {current : 'X'}
    fill_neighbors(current)
    dirs = {
        'N' : lambda x, y: ('-', (x,y-1), (x,y-2)),
        'S' : lambda x, y: ('-', (x,y+1), (x,y+2)),
        'W' : lambda x, y: ('|', (x-1,y), (x-2,y)),
        'E' : lambda x, y: ('|', (x+1,y), (x+2,y))
        }
    walk(data, current, 0)
    for k,v in grid.items():
        if v == '?':
            grid[k] = '#'
    paths = find_routes(grid, current)
    print((len(sorted(paths.items(), key = lambda x: -len(x[1]))[0][1])-1)//2)
    print(len([k for k,v in paths.items() if grid[k] == '.' and (len(v) -1) / 2 >= 1000]))
