def minimumSwaps(arr):
    cont = 0
    temp = [0] * len(arr)
    for index, value in enumerate(arr):
        temp[value-1] = index

    for i in range(len(arr)):
        if arr[i] != (i+1):
            t = temp[i]
            arr[i], arr[t] = i + 1, arr[i]
            temp[i], temp[arr[t]-1] = i, t
            cont += 1

    return cont



arr = [7, 1, 3, 2, 4, 5, 6 ]
print(minimumSwaps(arr))