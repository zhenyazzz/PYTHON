numbers = (5, 3, -1, 8, -4, 6)
numbers_list = list(numbers)
# for num in numbers_list:
#     if num < 0:
#         numbers_list.remove(num)
#         break
numbers_list.remove(next(num for num in numbers_list if num < 0))
numbers = tuple(numbers_list)
print(numbers)
