def multiply_all(l, v):
    return list(map(lambda x: x * num(v), l))

def num(v):
    return v

print(multiply_all([1, 2, 3], 3))