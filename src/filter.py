from map import numbers

even_list = filter(lambda num: num%2 == 0, numbers)
print(list(even_list))