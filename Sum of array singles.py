def repeats(arr):

    return sum(filter(lambda x: arr.count(x) < 2, arr))


print(repeats([1, 2, 2, 3]))