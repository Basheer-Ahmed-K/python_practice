from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 9]

total = reduce(lambda acc, curr: acc + curr, numbers)
print(total)
print(sum(numbers))


names = ["basheer ahmed", "Krishna", "Kuldeep", "Maanvi", "Prathiba", "kalai", "Amit"]

char_count = reduce(lambda arr, curr: arr + len(curr), names, 0)
print(char_count)