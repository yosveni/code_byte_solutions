def taskOfPairing(freq):
    weight_dic = {}
    suma = 0
    for i, f in enumerate(freq):
        weight = i + 1
        if i > 0 and i % 2 != 0 and freq[i-1] % 2 != 0:
            residual = 1
        weight_dic[weight] = f // 2

    for value in weight_dic.values():
        suma += value

    return suma + residual


freq = [3, 5, 6, 2]

print(taskOfPairing(freq))