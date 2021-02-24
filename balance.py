class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# def isBalanced(cad):
#     p = Stack()
#     balanced = True
#     index = 0
#     while index < len(cad) and balanced:
#         symbol = cad[index]
#         if symbol == "(":
#             p.add(symbol)
#         else:
#             if p.isEmpty():
#                 balanced = False
#             else:
#                 p.pop()
#
#         index += 1
#
#     if balanced and p.isEmpty():
#         return True
#     else:
#         return False



def isBalancedExtend(cad):
    p = Stack()
    balanced = True
    index = 0
    while index < len(cad) and balanced:
        symbol = cad[index]
        if symbol in "([{":
            p.add(symbol)
        else:
            if p.isEmpty():
                balanced = False
            else:
                top = p.pop()
                if not isCouples(top, symbol):
                       balanced = False
        index = index + 1
    if balanced and p.isEmpty():
        return True
    else:
        return False


def isCouples(symbolOpen, symbolClose):
    opens = "([{"
    closes = ")]}"
    return opens.index(symbolOpen) == closes.index(symbolClose)



print(isBalancedExtend('{{([][])}()}'))
print(isBalancedExtend('[{()]'))