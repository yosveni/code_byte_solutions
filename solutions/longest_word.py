import re
def LongestWord(sen):
    cleanString = re.compile('\W+')
    res = cleanString.split(sen)
    print(res)
    return max(res, key=len)

# def KUniqueCharacters(strParam):
#     firt_char = strParam[0]
#     for i in range(1, len(strParam)):
#
#     return firt_char
MAX_SIZE = 26
def isValid(count, k):
   val = 0
   for i in range(MAX_SIZE):
      if count[i] > 0:
         val += 1
   return (k >= val)

def KUniqueCharacters(strParam):
   unique = 0
   k = int(s[0])
   strParam= strParam[1:]
   size = len(strParam)
   count = [0] * MAX_SIZE
   for i in range(size):
      if count[ord(strParam[i])-ord('a')] == 0:
         unique += 1
      count[ord(strParam[i])-ord('a')] += 1

   if unique < k:
      return

   start = 0
   end = 0
   window_length = 1
   window_start = 0
   count = [0] * len(count)
   count[ord(strParam[0])-ord('a')] += 1
   for i in range(1, size):
      count[ord(s[i])-ord('a')] += 1
      end+=1
      while not isValid(count, k):
         count[ord(strParam[start])-ord('a')] -= 1
         start += 1
      if end-start+1 > window_length:
         window_length = end-start+1
         window_start = start

   return strParam[window_start:window_start + window_length]

s = "3ppqprqtqtqt"
k = 3
print(KUniqueCharacters(s))