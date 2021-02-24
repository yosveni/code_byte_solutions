def pairs(k, arr):
    myDict = {item: 1 for index, item in enumerate(arr)}
    count = 0
    for each in myDict:
        if each + k in myDict:
            count += 1
    print(count)


arr = [1 ,5, 3, 4 ,2]
k = 2

pairs(k,arr)



