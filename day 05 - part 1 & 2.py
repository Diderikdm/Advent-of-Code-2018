def find(data):
    while True:
        start = len(data)
        for x in range(ord('a'), ord('z') + 1):
            data = data.replace(chr(x) + chr(x - 32), '').replace(chr(x - 32) + chr(x), '')
        if len(data) == start:
            return data

with open("2018day5.txt", 'r') as file:
    data = file.read()
    calc = lambda x, y: abs(ord(x) - ord(y)) - 32 == 0
    print(len(find(data)))
    letters = {}
    for x in range(ord('a'), ord('z') + 1):
        temp = data.replace(chr(x), '').replace(chr(x - 32), '')
        letters[chr(x)] = find(temp)
    print(min(len(x) for x in letters.values()))
