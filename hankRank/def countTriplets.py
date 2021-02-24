from collections import defaultdict
def countTriplets(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k * r] += v2[k]
        v2[k * r] += 1
    print(count)


arr = [1, 2, 2, 4]
countTriplets(arr, 2)