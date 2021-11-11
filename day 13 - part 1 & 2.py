with open("2018 day13.txt", 'r') as file:
    data = file.read().splitlines()
    grid = {}
    carts = {}
    cs = '<>^v'
    nexts = {'^' : lambda x,y : (x,y-1), 'v' : lambda x,y : (x,y+1), '<' : lambda x,y : (x-1,y), '>' : lambda x,y : (x+1,y)}
    dirs = [{'^' : '<', '<' : 'v', 'v' : '>', '>' : '^'}, {'^' : '^', '<' : '<', 'v' : 'v', '>' : '>'}, {'^' : '>', '<' : '^', 'v' : '<', '>' : 'v'}]
    corners = {'\\' : {'^' : '<', '<' : '^', '>' : 'v', 'v': '>'}, '/' : {'^' : '>', '>': '^', '<' : 'v', 'v' : '<'}}
    for y, row in enumerate(data):
        for x, what in enumerate(row):
            grid[(x,y)] = what if what not in cs else ''
            if what in cs:
                carts[(x,y)] = {'Cart' : what, 'Dir' : 0}
    p1 = None
    while len(carts) > 1:
        crashes = set()
        next_carts = {}
        for k,v in sorted(carts.items()):
            nxt = nexts[v['Cart']](*k)
            grd = grid[nxt]
            if k not in next_carts and nxt not in next_carts:
                next_carts[nxt] = carts[k]
                if grd in corners:
                    next_carts[nxt]['Cart'] = corners[grd][carts[k]['Cart']]
                elif grd == '+':
                    next_carts[nxt]['Cart'] = dirs[carts[k]['Dir']][carts[k]['Cart']]
                    next_carts[nxt]['Dir'] = (carts[k]['Dir'] + 1) % 3
            else:
                crash = next(iter(x for x in [k, nxt] if x in next_carts))
                p1 = p1 or ','.join([str(x) for x in crash])
                crashes.add(crash)
        for x in crashes:
            next_carts.pop(x)
        crashes = set()
        carts = next_carts
    print(p1)
    print(','.join([str(x) for x in next(iter(carts))]))
