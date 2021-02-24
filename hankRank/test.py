def StockPicker(arr):
    minpos = arr.index(min(arr))
    max_rofit = 0
    for pos in range(minpos+1, len(arr)):
        if arr[pos] > arr[minpos]:
           rest = arr[pos] - arr[minpos]
           if rest > max_rofit:
              max_rofit = rest

    return max_rofit


arr = [10, 12, 4, 5, 9]

print(StockPicker(arr))
