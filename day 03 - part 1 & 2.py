with open("2018day3.txt", 'r') as file:
    data = [x.split('@ ')[1] for x in file.read().splitlines()]
    grid = {}
    for elf in data:
        s, r = elf.split(': ')
        sx, sy = [int(x) for x in s.split(',')]
        rx, ry = [int(x) for x in r.split('x')]
        for coord in sum([[(x,y) for x in range(sx, sx + rx)] for y in range(sy, sy + ry)], []):
            if coord not in grid:
                grid[coord] = 0
            grid[coord] += 1
    print(sum(1 for x in grid.values() if x > 1))
    for elf in data:
        s, r = elf.split(': ')
        sx, sy = [int(x) for x in s.split(',')]
        rx, ry = [int(x) for x in r.split('x')]
        for coord in sum([[(x,y) for x in range(sx, sx + rx)] for y in range(sy, sy + ry)], []):
            if not any(grid[z] != 1 for z in sum([[(x,y) for x in range(sx, sx + rx)] for y in range(sy, sy + ry)], [])):
                print(data.index(elf) + 1)
                break
        else:
            continue
        break
