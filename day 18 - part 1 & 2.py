with open("2018day18.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    grid = {(x,y) : data[y][x] for x in range(len(data[0])) for y in range(len(data))}
    adj = lambda x,y: set(sum([[(a,b) for a in range(x-1,x+2) if (a,b) != (x,y) and (a,b) in grid] for b in range(y-1,y+2)], []))
    i = 1
    scores = []
    while True:
        new_grid = {}
        for k,v in grid.items():
            if v == '.':
                if len([x for x in adj(*k) if grid[x] == '|']) >= 3:
                    new_grid[k] = '|'
                else:
                    new_grid[k] = '.'
            elif v == '|':
                if len([x for x in adj(*k) if grid[x] == '#']) >= 3:
                    new_grid[k] = '#'
                else:
                    new_grid[k] = '|'
            else:
                ad = [grid[x] for x in adj(*k)]
                if '|' in ad and '#' in ad:
                    new_grid[k] = '#'
                else:
                    new_grid[k] = '.'
        grid = new_grid
        score = len([k for k,v in grid.items() if v == '|']) * len([k for k,v in grid.items() if v == '#'])
        if i == 10:
            print(score)
        if score in scores:
            prev = scores[::-1].index(score)
            if all(scores[x] == scores[x-prev-1] for x in range(-prev-1,0)):
                res = scores[-prev-1:]
                break
        scores.append(score)
        i+=1
    print(res[((1000000000-i) % len(res))])
