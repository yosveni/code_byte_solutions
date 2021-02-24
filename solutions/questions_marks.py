def QuestionsMarks(strParam):
    cont = 0
    isValid = 'false'
    num_temp = 0
    for pos, char in enumerate(strParam):
        if char.isdigit():
          num_temp += int(char)
          if cont == 3 and num_temp == 10:
              if len(strParam) == pos + 1:
                  isValid = 'true'
                  break
              else:
                  cont = 0
                  num_temp = int(char)
                  continue
          else:
              cont = 0
              isValid = 'false'
              num_temp = int(char)
        elif char == '?':
             cont += 1

    return isValid







   # code goes here
   # return strParam



strParam = "9???1???9??1???9"
print(QuestionsMarks(strParam))