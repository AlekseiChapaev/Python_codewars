def transpose_two_strings(arr):
    if len(arr[0]) > len(arr[1]):
        arr[1] = arr[1].ljust(len(arr[0]))
    else:
        arr[0] = arr[0].ljust(len(arr[1]))
    res = ''
    for i in range(0, len(arr[0])):
         res += f'{(arr[0])[i]} {(arr[1])[i]}\n'

    return res[:-1]
print(transpose_two_strings(["Hello","World"]))

