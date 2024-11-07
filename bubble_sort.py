array = [5, 4, 3, 2, 1]


def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length - 1):
            if array[j] > array[j + 1]:
                # array[j], array[j + 1] = array[j + 1], array[j]
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


bubble_sort(array)
print(array)
