def matchingStrings(strings, queries):
    result = {}
    response = []
    for elem in strings:
        if elem in strings:
            result[elem] = result.get(elem, 0) + 1
        else:
            result[elem] = 1

    for val in queries:
        if val in result:
            response.append(result[val])
        else:
            response.append(0)

    return response


    return list(result.values())

string = ['aba', 'baba', 'aba','xzxb']
queries = ['aba', 'xzxb', 'ab']

print(matchingStrings(string,queries))