"""
Перемещение нулей в массиве

Необходимо написать функцию, которая берет массив и перемещает все нули в конец,
сохраняя порядок остальных элементов.

Пример вывода функции:

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(nums):
    zeros_count = nums.count(0)
    for _ in range(zeros_count):
        nums.remove(0)
        nums.append(0)
    return nums


print(move_zeros([0, 0, 1, 1, 2, 1, 3]))
print(move_zeros([1, 0, 1, 2, 0, 1, 3, 0]))
print(move_zeros([1, 1, 2, 1, 3]))
print(move_zeros([0, 0, 0, 0]))
