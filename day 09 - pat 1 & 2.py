with open("2018day9.txt", 'r') as file:
    data = [int(x) for x in file.read().split() if x.isdigit()]
    ll = {0 : 0}
    rll = {0 : 0}
    players = {x : 0 for x in range(1, data[0]+1)}
    player = 0
    current = 0
    for x in range(1, data[1] * 100 + 1):
        player = player % data[0] + 1
        if x % 23 != 0:
            k = ll[current]
            v = ll[k]
            ll[k] = x
            ll[x] = v
            rll[v] = x
            rll[x] = k
            current = x
        else:
            for y in range(7):
                current = rll[current]
            k = rll[current]
            v = ll[current]
            players[player] += x + current
            ll[k] = ll.pop(current)
            rll[v] = rll.pop(current)
            current = ll[k]
        if x == data[1]:
            print(max(players.values()))    
    print(max(players.values()))
