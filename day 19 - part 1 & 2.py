with open("2018day19.txt", 'r') as file:
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
    ln = len(instructions)
    p2 = False
    for registers in [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]]:
        while registers[ip] < ln:
            ins = instructions[registers[ip]]
            registers[ins[3]] = ops[ins[0]](registers, ins, None)
            registers[ip] += 1
            if p2 and 2 < registers[ip] < 10:
                mx = max(registers)
                print(sum([x for x in range(1, mx+1) if not mx%x]))
                break
        if not p2:
            print(registers[0])
        p2 = True
