data = '939601'
recipes = '37'
e1, e2, data_len = 0,1, len(data)+1
while data not in recipes[-data_len:]:
    recipes += str(int(recipes[e1]) + int(recipes[e2]))
    amt = len(recipes)
    e1 = (e1 + 1 + int(recipes[e1])) % amt
    e2 = (e2 + 1 + int(recipes[e2])) % amt
print(recipes[int(data): int(data) + 10])
print(recipes.index(str(data)))
