def sherlockAndAnagrams(s):
    anagrams = {}
    length = len(s)
    for i in range(length):
        for j in range(i, length):
            word = s[i:j + 1]
            word = ''.join(sorted(word))
            anagrams[word] = anagrams.get(word, 0) + 1
    cont = 0
    for word in anagrams:
        value = anagrams[word]
        cont += (value * (value - 1)) // 2

    print(cont)


s = 'abba'
sherlockAndAnagrams(s)
