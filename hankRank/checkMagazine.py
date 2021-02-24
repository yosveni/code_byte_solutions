def checkMagazine(magazine, note):
    answer = 'No'
    magazine_dic = {}
    for word in magazine:
        if word not in magazine_dic:
            magazine_dic[word] = 1
        else:
            magazine_dic[word] = magazine_dic[word] + 1

    for word in note:
        if word not in magazine_dic:
            answer = 'No'
        else:
            magazine_dic[word] = magazine_dic[word] - 1

            if magazine_dic[word] < 0:
                answer = 'No'
                break
            else:
                answer = 'Yes'
    return answer







"""
give me one grand today night
give one grand today
"""

# magazine = ['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts']
# note = ['ive', 'got', 'some', 'coconuts']
magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
note = ['give', 'one', 'grand', 'today']

# magazine = ['two', 'times', 'three', 'is', 'not', 'four']
# note = ['two', 'times', 'two', 'is', 'four']

print(checkMagazine(magazine, note))