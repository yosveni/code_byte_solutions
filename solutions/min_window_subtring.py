from collections import Counter


def MinWindowSubstring(strArr):
    s = strArr[0]
    t = strArr[1]
    dict_t = Counter(t)
    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))
    l, r = 0, 0
    formed = 0
    window_counts = {}
    required = len(dict_t)
    ans = float("inf"), None, None
    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1

        if window_counts[character] == dict_t[character]:
            formed += 1

        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while l <= r and formed == required:
            character = filtered_s[l][1]

            # Save the smallest window until now.
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1

        r += 1
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]