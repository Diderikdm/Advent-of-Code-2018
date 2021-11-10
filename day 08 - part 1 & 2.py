def calc(data, index = 0):
    children, metadata = data[index : index + 2]
    index += 2
    child_values = 0
    if children:
        child_result = []
        for x in range(children):
            child_value, index = calc(data, index)
            child_result += [child_value]
        for i in data[index : index + metadata]:
            child_values += child_result[i - 1 : i][0] if child_result[i - 1 : i] else 0
    else:
        child_values = sum(data[index : index + metadata])
    metadatas.append(sum(data[index : index + metadata]))
    index += metadata
    return child_values, index
    
with open("2018day8.txt", 'r') as file:
    data = [int(y) for y in sum([x.split() for x in file.read().splitlines()], [])]
    metadatas = []
    ans = calc(data)[0]
    print(sum(metadatas))
    print(ans)
