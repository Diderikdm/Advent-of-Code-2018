from datetime import datetime
from datetime import timedelta

with open("2018day4.txt", 'r') as file:
    data = {y : z for y,z in [x.strip('[').split('] ') for x in file.read().splitlines()]}
    guards = {}
    for k,v in sorted(data.items()):
        if 'Guard' in v:
            guard = int(v.split(' ')[1].strip('#'))
            if guard not in guards:
                guards[guard] = []
        elif 'falls' in v:
            sleep_date = datetime.strptime(k, '%Y-%m-%d %H:%M')
        elif 'wakes' in v:
            wake_date = datetime.strptime(k, '%Y-%m-%d %H:%M')
            while sleep_date != wake_date:
                guards[guard].append(int(str(sleep_date).split(':')[1]))
                sleep_date += timedelta(minutes=1)
    mx = max(guards.items(), key = lambda x: len(x[1]))
    print(mx[0] * max(mx[1], key = lambda x: mx[1].count(x)))
    nmx = max(guards.items(), key = lambda x: max(x[1].count(i) for i in range(60)))
    print(nmx[0] * max(nmx[1], key = lambda x: nmx[1].count(x)))
