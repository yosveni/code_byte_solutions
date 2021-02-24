def solution(A):
    m = max(A)
    if m < 1:
       return 1

    A = set(A)
    B = set(range(1, m + 1))
    D = B - A
    if len(D) == 0:
        return m + 1
    else:
        return min(D)



def sol(T):
   middle = len(T) // 2
   arr = T[middle:]
   temp = set([T[i] for i in range(middle)])
   if len(temp) < len(arr):
       for elem in arr:
           if elem is not temp:
               temp.add(elem)

   return len(temp)


# def sol2(N):
#     products = []
#     power = 1
#     while power < N:
#         prod_power = power
#         while prod_power < N:
#             products.append(prod_power)
#             prod_power *= 3
#         power *= 2
#     products.sort()
#     return products


def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

import numpy as np
def solu3(index, K):
   test = []
   train = []
   split_list = np.array_split(index, K)
   for elem in split_list:
       if list(elem) is not test:
           test.append(list(elem))
       train.append(list(elem))

   return test + list(reversed(train))

print(solu3([1, 2, 3,6,8], 4))
