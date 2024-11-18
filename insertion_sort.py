array = [5, 4, 3, 2, 1]


def insertion_sort(array):
    length = len(array)
    for i in range(1, length):
        sorted = True
        j = i - 1
        while j >= 0:
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                sorted = False
                print(array)
            j = j - 1

        if sorted:
            break


insertion_sort(array)
print(array)
