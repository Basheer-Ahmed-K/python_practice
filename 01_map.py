def change_even(n):
    if n%2 == 1:
        return n+1
    else:
        return n

x = [535, 431, 543, 457, 901, 345]

y = list(map(change_even, x))
print(y)