def ReverseString(cad):
    aux = cad[len(cad)::-1]
    if aux == cad:
        return True
    else:
        return False
    # return


cad = 'abc'

print(ReverseString(cad))