def solution(args):
    res = []
    if args:
        tmp, i, ln = args[0], 0, len(args)
        while i < ln:
            tmp, j = args[i], i
            while j < ln - 1 and args[j+1] == args[j]+1:
                j += 1
            if j - i > 1:
                tmp = str(args[i]) + "-" + str(args[j])
                i = j+1
            else:
                i = (j if j > i else i+1)
            res.append(tmp)
    return ",".join(str(x) for x in res)





arr =[ -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]

print(solution(arr))