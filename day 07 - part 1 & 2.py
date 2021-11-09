from collections import defaultdict

with open("2018day7.txt", 'r') as file:
    data = [(y[1], y[-3]) for y in [x.split() for x in file.read().splitlines()]]
    pre = defaultdict(list)
    req = defaultdict(list)
    ans = ''
    done = {}
    for x,y in data:
        pre[x].append(y)
        req[y].append(x)
        done[x] = False
    grid = sorted([k for k in pre.keys() if k not in sum(pre.values(), [])])
    while not all(x for x in done.values()):
        grid = sorted([x for x in list(set(grid + [k for k,v in req.items() if all(done[z] for z in v)])) if x not in ans])
        current = grid[0]
        done[current] = True
        ans += current  
    ans += next(iter(k for k in req if k not in ans))
    print(ans)
    done = {x[0] : False for x in data}
    grid = sorted([k for k in pre.keys() if k not in sum(pre.values(), [])])
    t = -1
    cur = {}
    ans2 = ''
    while not all(x for x in done.values()):
        t += 1
        dn = {k:v for k,v in cur.items() if k == t}
        for k,v in dn.items():
            cur.pop(k)
            done[v] = True
            ans2 += v
        grid = sorted([x for x in list(set(grid + [k for k,v in req.items() if all(done[z] for z in v)])) if x not in ans2 and x not in cur.values()])
        for x in range(5 - len(cur)):
            if grid:
                cur[t + 60 + ord(grid[0]) % (ord('A') -1)] = grid[0]
                grid = grid[1:]
    print(t + 60 + ord(next(iter(k for k in req if k not in ans2))) % (ord('A') -1))
