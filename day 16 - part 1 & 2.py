with open("2018day16.txt", 'r') as file:
    data = [x for x in file.read().split('\n\n') if x]
    prog = data.pop(-1)
    prog = [tuple(eval('[{}]'.format(','.join(op.split())))) for op in prog.splitlines()]
    check = lambda b, o, a: all(b[x] == a[x] for x in range(4) if x != o[3])
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
    result = set()
    ans = 0
    for row in data:
        before, op, after = [x.strip('Before:').strip('After:').strip() for x in row.splitlines()]
        before, op, after = [tuple(eval(before)), tuple(eval('[{}]'.format(','.join(op.split())))), tuple(eval(after))]
        temp = [k for k,v in ops.items() if v(before, op, after) == after[op[3]]]
        result.add((op[0], tuple([x for x in temp])))
        if len(temp) >= 3:
            ans += 1
    print(ans)
    opcodes = {}
    while len(opcodes) < len(ops):
        for op, res in sorted(result, key = lambda x: len(x[1])):
            f_ops = [x for x in res if x not in opcodes.values()]
            if len(f_ops) == 1:
                opcodes[op] = f_ops[0]
    before = [0, 0, 0, 0]
    for op in prog:
        after = before
        after[op[3]] = ops[opcodes[op[0]]](before, op, after)
        before = [x for x in after]
    print(after[0])
