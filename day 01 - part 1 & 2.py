with open("2018day1.txt", 'r') as file:
    data = [int(x) for x in file.read().splitlines()]
    print(sum(data))
    fr, frs, i = 0, set(), 0
    while fr not in frs:
        frs.add(fr)
        fr = fr + data[i % len(data)]
        i += 1
    print(fr)
