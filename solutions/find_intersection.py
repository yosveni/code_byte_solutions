def FindIntersection(strArr):
    firstList = set(strArr[0].split(", "))
    twoList = set(strArr[1].split(", "))
    result = list(firstList.intersection(twoList))
    listConverted = sorted([int(i) for i in result])
    if len(listConverted) == 0:
      return 'false'
    else:
      return ','.join(str(ele) for ele in listConverted)

    return result
