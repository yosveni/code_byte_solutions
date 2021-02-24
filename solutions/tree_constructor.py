def TreeConstructor(strArr):
    tree = [eval(i) for i in strArr]
    parent = [elem[1] for elem in tree]
    isValid = "true"
    if len(tree) < 2:
        isValid = 'false'
    parents = dict()
    for i in parent:
        parents[i] = parents.get(i, 0) + 1

    for elem in parents:
        if parents[elem] > 2:
            isValid = 'false'
            break

    return isValid