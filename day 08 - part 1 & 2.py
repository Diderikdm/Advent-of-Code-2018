def calc(lst, i = 0):
    children = lst[i]
    md = lst[i + 1]
    i += 2
    temp = []
    sm = 0
    if children:
        for x in range(children):
            s, i = calc(lst, i)
            temp += [s]
        for x in lst[i : i + md]:
            sm += temp[x - 1 : x][0] if temp[x - 1 : x] else 0
    else:
        sm = sum(lst[i : i + md])
    metadata.append(sum(lst[i : i + md]))
    i += md
    return sm, i
    
with open("2018day8.txt", 'r') as file:
    data = [int(y) for y in sum([x.split() for x in file.read().splitlines()], [])]
    metadata = []
    ans = calc(data[:])[0]
    print(sum(metadata))
    print(ans)
