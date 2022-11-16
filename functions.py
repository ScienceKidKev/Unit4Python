def hello_world():
    print('hello world')

hello_world()

#add, subtract, divide, remainder, exponent#
def add(a, b):
    print(a+b)


add(9, 10)

def subtract(a, b):
    print(a-b)

subtract(5, 2)

def divide(a, b):
    print(a/b)

divide(49, 7)

def remainder(a, b):
    print(a%b)

remainder(50, 7)

def exponent(a, b):
    print(a**b)

exponent(2, 5)

#slope#
def slope(m, x, b):
    return m*x+b

y= slope(10, 9, 8)
print(y)
