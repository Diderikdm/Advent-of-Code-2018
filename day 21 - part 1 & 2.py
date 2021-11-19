with open("2018 day21.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    ip = int(data[0].split()[1])
    instructions = [[int(x) if x.isdigit() else x for x in y.split()] for y in data[1:]]
    ops = {
        'addr' : lambda b, o, a: b[o[1]] + b[o[2]],
        'addi' : lambda b, o, a: b[o[1]] + o[2],
        'mulr' : lambda b, o, a: b[o[1]] * b[o[2]],
        'muli' : lambda b, o, a: b[o[1]] * o[2],
        'banr' : lambda b, o, a: b[o[1]] & b[o[2]],
        'bani' : lambda b, o, a: b[o[1]] & o[2],
        'borr' : lambda b, o, a: b[o[1]] | b[o[2]],
        'bori' : lambda b, o, a: b[o[1]] | o[2],
        'setr' : lambda b, o, a: b[o[1]],
        'seti' : lambda b, o, a: o[1],
        'gtir' : lambda b, o, a: (1 if o[1] > b[o[2]] else 0),
        'gtri' : lambda b, o, a: (1 if b[o[1]] > o[2] else 0),
        'gtrr' : lambda b, o, a: (1 if b[o[1]] > b[o[2]] else 0),
        'eqir' : lambda b, o, a: (1 if o[1] == b[o[2]] else 0),
        'eqri' : lambda b, o, a: (1 if b[o[1]] == o[2] else 0),
        'eqrr' : lambda b, o, a: (1 if b[o[1]] == b[o[2]] else 0)
        }
    prev = set()
    b8 = 2 ** 8
    b16 = 2 ** 16
    b24 = 2 ** 24
    x, y = instructions[7][1], instructions[11][2]
    i = 0
    p1, p2 = None, None
    while not p1 or not p2:
        trial = i | b16
        i = x
        while True:
            i = (((i + (trial & (b8 - 1))) & (b24 - 1)) * y) & (b24 - 1)
            if b8 > trial:
                p1 = p1 or i
                if i in prev:
                    p2 = temp
                    break 
                prev.add(i)
                temp = i
                break
            else:
                trial //= b8
    print(p1)
    print(p2)
