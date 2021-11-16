from collections import deque

def __print(e, i):
    print(e, i)
    t = ''
    for y in range(len(data)):
        for x in range(len(data[0])):
            t += grid[(y,x)]
        t += ','.join([str(z[1]) for z in chars.items() if z[0][0] == y])
        t += '\n'
    print(t)    

def find_fighters(char, info, chars):
    y, x = char
    return next(iter(sorted([(b,a) for a,b in ((x,y-1), (x-1,y), (x+1,y), (x,y+1)) if (b,a) in chars and chars[(b,a)][0] == ('E' if info[0] == 'G' else 'G')],
                            key = lambda z: (chars[z][1], z))), None)


def find_goals(grid, char_to_find):
    goals = set()
    for coord, what in filter(lambda x: x[1][0] == char_to_find, grid.items()):
        y, x = coord
        for a, b in ((x,y-1), (x-1,y), (x+1,y), (x,y+1)):
            if grid[(b,a)] == '.':
                goals.add((b,a))
    return goals
    

def find_route(grid, start, info, goals, chars):
    for char in chars:
        if char != start:
            grid[char] = '#'
    paths = {}
    q = deque([[start]])
    prev = set([start])
    while q:
        path = q.popleft()
        y,x = path[-1]
        if len(paths) == len(goals):
            return paths
        if (y,x) in goals and (y,x) not in paths:
            paths[(y,x)] = [z for z in path]
        for a, b in ((x,y-1), (x-1,y), (x+1,y), (x,y+1)):
            if grid[(y,x)] != '#' and (b,a) not in prev:
                q.append(path + [(b,a)])
                prev.add((b,a))
    return paths


with open("2018day15.txt", 'r') as file:
    data = file.read().splitlines()
    print_board = False
    e = 3
    while True:
        grid = {(y,x) : data[y][x] for x in range(len(data[0])) for y in range(len(data))}
        i = 0
        chars = {(y,x) : [data[y][x], 200] for x in range(len(data[0])) for y in range(len(data)) if grid[(y,x)].isalpha()}
        while True:
            if print_board:
                __print(e, i)         
            c_round = {k:v for k,v in chars.items()}
            done = False
            for char, info in sorted(c_round.items(), key = lambda x: x[0]):
                if char not in chars:
                    continue
                if done:
                    break
                fighter = find_fighters(char, info, chars)
                if not fighter:
                    goals = find_goals(grid, 'E' if info[0] == 'G' else 'G')
                    paths = find_route({k:v for k,v in grid.items()}, char, info, goals, chars)
                    if paths:
                        path = next(iter(sorted(paths.items(), key = lambda x: (len(x[1]), x[1][-1]))), None)
                        if path:
                            path = path[1][1]
                            grid[path] = grid.pop(char)
                            grid[char] = '.'
                            chars[path] = chars.pop(char)
                            fighter = find_fighters(path, info, chars)
                if fighter:
                    chars[fighter][1] -= 3 if info[0] == 'G' else e
                    if chars[fighter][1] <= 0:
                        chars.pop(fighter)
                        grid[fighter] = '.'
                        if len(set([x[0] for x in chars.values()])) < 2:
                            done = True
            else:
                i += 1
                if len(set([x[0] for x in chars.values()])) < 2:
                    break
                continue
            break
        if e == 3:
            print(i * sum([x[1] for x in chars.values()]))
        e += 1
        if len([k for k,v in chars.items() if v[0] == 'E']) == ''.join(data).count('E'):
            print(i * sum([x[1] for x in chars.values()]))
            break
