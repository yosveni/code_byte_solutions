def arrayManipulation(n, queries):
    array = [0] * (n + 1)

    for query in queries:
        a = query[0] - 1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k

    maxx= 0
    count = 0
    for i in array:
        count += i
        if count > maxx:
            maxx = count

    return maxx



n = 5
queries = [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100]
]

print(arrayManipulation(n, queries))