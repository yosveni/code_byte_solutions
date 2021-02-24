def PermutationStep(num):
    numbers = [int(x) for x in str(num)]
    size = len(numbers)
    for i in range(size - 1, 0, -1):
        if numbers[i] > numbers[i - 1]:
            break
    if i == 1 and numbers[i] <= numbers[i - 1]:
        return

    num = numbers[i - 1]
    num_small = i
    for j in range(i + 1, size):
        if numbers[j] > num and numbers[j] < numbers[num_small]:
            num_small = j

    numbers[num_small], numbers[i - 1] = numbers[i - 1], numbers[num_small]
    num = 0

    for k in range(i):
        num = num * 10 + numbers[k]

    numbers = sorted(numbers[i:])

    for l in range(size - i):
        num = num * 10 + numbers[l]

    return num


def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (sum(s[n // 2 - 1:n // 2 + 1]) / 2.0, s[n // 2])[n % 2] if n else None


def MovingMedian(arr):
    new_arr = arr[1:]
    result = []
    for i in new_arr:
        median_temp = []
        num = i
        while num > 0:
           median_temp.append(num)
           num -= 1
        result.append(median(median_temp))

    return result


def Wildcards(strParam):
    result = [x.strip() for x in strParam.split(' ')]
    pattern = result[0]
    strParam = result[1]
    pattern_size = len(pattern)
    strr_size = len(strParam)

    matrix_zero = [[False for i in range(pattern_size+1)] for j in range(strr_size+1)]
    strParam = " " + strParam
    pattern = " " + pattern
    matrix_zero[0][0] = True

    for i in range(1, pattern_size + 1):
        if (pattern[i] == '*'):
            matrix_zero[0][i] = matrix_zero[0][i-1]
    for i in range(1, strr_size + 1):
        for j in range(1, pattern_size + 1):
            if strParam[i] == pattern[j] or pattern[j] == '+':
                matrix_zero[i][j] = matrix_zero[i-1][j-1]
            elif pattern[j] == '*':
                matrix_zero[i][j] = max(matrix_zero[i-1][j],  matrix_zero[i][j-1])

    return matrix_zero[strr_size][pattern_size]

strr =  "$**+*{2} 9mmmrrrkbb"
# pattern = "*****ba*****ab"
# char pattern[] = "ba*****ab"
# char pattern[] = "ba*ab"
# char pattern[] = "a*ab"
# char pattern[] = "a*****ab"
# char pattern[] = "*a*****ab"
# char pattern[] = "ba*ab****"
# char pattern[] = "****"
# char pattern[] = "*"
# char pattern[] = "aa?ab"
# char pattern[] = "b*b"
# char pattern[] = "a*a"
# char pattern[] = "baaabab"
# char pattern[] = "?baaabab"
# char pattern[] = "*baaaba*"

print(Wildcards(strr))

# num = "+++++* abcdehhhhhh"
# print(num.split(" "))
