def avg(*args):
    cont = 0
    for num in args:
        cont += num
    return cont/len(args)




if __name__ == '__main__':
    # args = [2,5]
    # print(avg(2,5))
    print(avg(2, 5))
    # multiply(10, 9)
    # multiply(2, 3, 4)
    # multiply(3, 5, 10, 6)