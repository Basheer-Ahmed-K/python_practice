# Higher Order function: a function that either
#                         1. returns a function
#                         2. accepts a function as an parameter

def divisor(x):
    def divident(y):
        return y/x
    return divident # returns a functions so it is a higher order functions

divide = divisor(2)
print(divide(10))

def loud(text):
    return text.upper()
def quite(text):
    return text.lower()

def say(func): # This function is a higher order functions becz it is accepting function as an arg
    return func("Hello Guys!!")

output = say(quite)
print(output)