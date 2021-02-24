def balancedSums(arr):
    summy = sum(arr)
    l = len(arr)
    lefty = 0
    for i in range(len(arr)):
        current = arr[i]
        summy -= current
        if lefty == summy:
            return 'YES'
        lefty += current
    return 'NO'


arr = [1, 2, 3]
print(balancedSums(arr))