def repeats(arr):

    return sum(filter(lambda x: arr.count(x) < 2, arr))

print(repeats([16, 0, 11, 4, 8, 16, 0, 11]))

