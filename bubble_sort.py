import random


def bubbleSort(array):
    length = len(array)
    sorted = False

    for i in range(length):
        sorted = True

        for j in range(length - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                sorted = False

        if sorted:
            break


list = [random.randint(0, 100) for _ in range(100)]

bubbleSort(list)
print(list)
