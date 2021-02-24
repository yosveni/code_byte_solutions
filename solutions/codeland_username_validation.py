# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.

def CodelandUsernameValidation(strParam):
    isValid = 'true'
    if len(strParam) < 4 or len(strParam) > 25:
        isValid = 'false'
    elif not strParam[0].isalpha():
        isValid = 'false'
    elif strParam[len(strParam)-1] == '_':
        isValid = 'false'
    else:
        for char in strParam:
            if not (char.isalnum() or char.isdigit() or char=='_'):
                isValid = 'false'
                break
            else:
                isValid = 'true'
    return isValid

cad = "u__hello_world123"
print(cad[len(cad)-1])
print(CodelandUsernameValidation(cad))