class LetterFilter:

    def __init__(self, s):
        self.s = s
        self.vowels = ['a', 'e', 'i', 'o', 'u']

    def filter_vowels(self):
        consonants = ''
        for char in self.s:
            if char not in self.vowels:
                consonants += char
        return consonants

    def filter_consonants(self):
        vowels = ''
        for char in self.s:
            if char in self.vowels:
                vowels += char
        return vowels


# Enter your code here
# Return a string

# s = "onomatopoeia"
# f = LetterFilter(s)
# print(f.filter_vowels())
# print(f.filter_consonants())

a = set()
a.add(1)
a.add(2)
a.add(9)
a.add(1)
a.add(2)
a.add(3)
a.add(1)
a.add(4)
a.add(1)
a.add(5)
a.add(7)

print(a)

