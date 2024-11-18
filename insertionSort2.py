array = [5, 4, 3, 2, 1]


def insertionSort(array):
    for i in range(1, len(array)):
        j = i - 1
        sorted = False
        while j >= 0 and not sorted:
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            else:
                sorted = True
            j = j - 1


insertionSort(array)
print(array)
