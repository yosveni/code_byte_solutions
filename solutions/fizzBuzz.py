def fizzBuzz(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0 and i % 5 !=0:
            print('Fizz')
        elif i % 5 == 0 and i % 3 !=0:
            print('Buzz')
        else:
            print(i)



# a = 0
# for b in range(0, 10, 2):
#     a += b + 1
# print(a)
# fizzBuzz(15)

def foo(n):
    for x in range(n):
        yield x**3

for x in foo(5):
    print(x)