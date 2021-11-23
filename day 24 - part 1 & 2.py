def fight(order, groups):
    sort_fight = sorted(order, key = lambda x: -x[0][-3])
    temp_groups = {k:v for k,v in groups.items() if k not in [x[1] for x in sort_fight]}
    dmg_group = {}
    for group, target in sort_fight:
        if group in groups:
            if group in dmg_group:
                group = dmg_group[group]
            if target:
                dmg = group[2] * group[0] * (2 if group[3] in target[-1] else 1) * (1 if group[3] not in target[-2] else 0)
                units = dmg // target[1]
                if units < target[0]:
                    temp_groups[tuple([target[0] - units] + [x for x in target[1:]])] = groups[target]
                    dmg_group[target] = tuple([target[0] - units] + [x for x in target[1:]])
                else:
                    groups.pop(target)
                    if target in dmg_group:
                        dmg_group.pop(target)
        else:
            if target:
                temp_groups[target] = groups[target]
    return temp_groups


def select_targets(groups):
    sort_groups = sorted(groups.items(), key = lambda x: (-(x[0][2] * x[0][0]), -x[0][-3]))
    picked = []
    targets = []
    for group, identifier in sort_groups:
        target = next(iter(sorted([k for k,v in groups.items() if v != identifier and k not in picked and group[3] not in k[-2]],
                                  key = lambda x: (-group[0] * group[2] * (2 if group[3] in x[-1] else 1), -(x[2] * x[0]), -x[4]))), None)
        if target:
            targets.append([group, target])
            picked.append(target)
        else:
            targets.append([group, None])
    return targets
    

def build_groups(raw_data, identifier, groups, e):
    for row in raw_data:
        uh, rest = row.split(' hit points')
        units, hp = [int(x) for x in uh.split() if x.isdigit()]
        iw, di = rest.split(' with an attack that does ')
        dmg, ini = [int(x) for x in di.split() if x.isdigit()]
        dmg = dmg + e if identifier == 'imm' else dmg
        type_dmg = di.split()[1]
        ims = tuple()
        weak = tuple()
        if '(' in iw:
            iw = iw.split('(')[1].strip(')')
            if iw.startswith('immune'):
                if 'weak' in iw:
                    i, w = iw.split('; ')
                    weak = tuple(w.split('weak to ')[1].split(', '))
                else:
                    i = iw
                ims = tuple(i.split('immune to ')[1].split(', '))
            elif iw.startswith('weak'):
                if 'immune' in iw:
                    w, i = iw.split('; ')
                    ims = tuple(i.split('immune to ')[1].split(', '))
                else:
                    w = iw
                weak = tuple(w.split('weak to ')[1].split(', '))
        groups[(units, hp, dmg, type_dmg, ini, ims, weak)] = identifier
    return groups


with open("2018day24.txt", 'r') as file:
    data = [x for x in file.read().split('\n\n')]
p1 = None
e = 0
while True:
    groups = {}
    groups = build_groups([x for x in data[0].splitlines()[1:] if x], 'imm', groups, e)
    groups = build_groups([x for x in data[1].splitlines()[1:] if x], 'inf', groups, e)
    while len(set(groups.values())) > 1:
        temp = groups
        order = select_targets({k:v for k,v in groups.items()})
        groups = fight(order, groups)
        if groups == temp:
            break
    if not p1:
        p1 = sum([k[0] for k,v in groups.items()])
        print(p1)
    elif len(set([x for x in groups.values()])) == 1 and 'imm' in groups.values():
        print(sum([k[0] for k,v in groups.items()]))
        break
    e += 1
