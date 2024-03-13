# Lambda function is a single expression that returns a value
# also lambda functions sometimes refers to anonomous
# it is used inside a function (when we dont need to use the function again)

square = lambda num: num * num

print(square(2))

addTwo = lambda num: num + 2

print(addTwo(3))

sum = lambda a, b: a + b

print(sum(2, 4))


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))


