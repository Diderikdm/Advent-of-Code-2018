def find(x):
    pos = [z for z in data if z not in prev and sum([abs(x[i] - z[i]) for i in range(4)]) <= 3]
    for y in pos:
        prev.add(y)
        find(y)

with open("2018day25.txt", 'r') as file:
    data = [tuple([int(y) for y in x.split(',')]) for x in file.read().splitlines()]
    c = 0
    prev = set()
    while len(prev) != len(data):
        x = next(iter([x for x in data if x not in prev]))
        prev.add(x)
        find(x)
        c += 1
    print(c)
