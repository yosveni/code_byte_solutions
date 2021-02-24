def minimumBribes(q):
    cont = 0
    Q = [P - 1 for P in q]
    for i,P in enumerate(Q):
        if P - i > 2:
            print('Too chaotic')
            return
        for j in range(max(P-1,0),i):
            if Q[j] > P:
                cont += 1
    print(cont)

q = [1,2,3,4,5]

minimumBribes(q)