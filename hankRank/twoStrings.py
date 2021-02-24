def twoStrings(s1, s2):
    answer = 'No'
    s1_set = set(list(s1))
    s2_set = set(list(s2))
    if len(s1_set.intersection(s2_set)) > 0:
        answer = 'Yes'
    return answer

