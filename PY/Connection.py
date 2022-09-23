def count(x):
    dct[x] = dct.get(x, 0) + 1
    return dct[x]


dct = {}
print(*[count(k) for k in input().split()])