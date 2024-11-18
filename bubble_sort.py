array = [1, 2, 3, 5, 4]


def bubble_sort(array):
    length = len(array)
    for i in range(length):
        sorted = True
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                # array[j], array[j + 1] = array[j + 1], array[j]
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                sorted = False

        if sorted:
            break

        print(array)


bubble_sort(array)
