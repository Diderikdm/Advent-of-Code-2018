from collections import defaultdict

with open("2018day12.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    states = defaultdict(lambda: '.', {e : x for e,x in enumerate(data[0].split(': ')[1])})
    keys = {x.split(' => ')[0] : x.split(' => ')[1] for x in data[2:]}
    sums = []
    i = 0
    while not sums[20:] or not all(sums[x] - sums[x-1] == sums[x-1] - sums[x-2] for x in range(-1, -6, -1)):
        i += 1
        mn = next(iter(x for x in range(min(states), max(states) + 1) if states[x] == '#'))
        mx = next(iter(x for x in range(max(states), min(states) - 1, -1) if states[x] == '#'))
        new_states = {}
        for e in range(mn - 2, mx + 3):
            new_states[e] = keys[''.join([states[x] for x in range(e - 2, e + 3)])]
        states.update(new_states)
        sums.append(sum(k for k,v in states.items() if v == '#'))
    print(sums[19])
    print(sums[i-1] + (sums[i-1] - sums[i-2]) * (50000000000 - i))
