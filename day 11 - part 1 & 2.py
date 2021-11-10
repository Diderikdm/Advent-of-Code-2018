from itertools import combinations

data = 18
combs = [x for x in list(set(combinations([-1,0,1]*2, 2)))]
grid = [[int(next(iter(x for x in str((((x + 10) * y) + data) * (x + 10))[-3:-2]), '0')) - 5 for x in range(0,301)] for y in range(0,301)]
adj = lambda x,y : sum(grid[y+a][x+b] for a,b in combs)
bests = {(x,y) : adj(x,y) for x in range(1,299) for y in range(1,299)}
print(','.join([str(k-1) for k in max(bests.items(), key = lambda x: x[1])[0]]))
bests = {}
for z in range(3,300):
    for y in range(300):
        for x in range(300):
            if y + z >= 300 or x + z >= 300:
                continue
            bests[(x,y,z)] = sum(sum(grid[b][x : x + z]) for b in range(y, y + z))
print(','.join([str(k) for k in max(bests.items(), key = lambda x: x[1])[0]]))
