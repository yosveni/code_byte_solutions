from collections import Counter

def makeAnagram(a, b):
    d1 = Counter(a)
    d2 = Counter(b)

    rest1 = (d1-d2)
    rest2 = (d2-d1)

    total = (d1 - d2) + (d2 - d1)

    return sum(total.values())


a = 'cde'
b = 'abc'

print(makeAnagram(a, b))