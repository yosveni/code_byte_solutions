def BracketMatcher(strParam):
    stack = []
    openbracket = ['(']
    cleanString = strParam.replace(" ", "")
    for char in cleanString:
        if char in openbracket:
            stack.append(char)
        elif char.isalpha() or char.isalnum():
            continue
        else:
          if not stack:
            return 0
          current_char = stack.pop()
          if current_char == '(':
              if char != ')':
                  return 0
    if stack:
        return 0
    else:
        return 1


strParam = "(c(oder)) b(yte)"
print(BracketMatcher(strParam))