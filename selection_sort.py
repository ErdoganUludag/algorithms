array = [5, 4, 3, 2, 1]


def selection_sort(array):
    length = len(array)

    for i in range(length):
        sorted = True
        minimum = i
        for j in range(i + 1, length):
            if array[j] < array[minimum]:
                minimum = j
                sorted = False

        if sorted:
            break

        array[minimum], array[i] = array[i], array[minimum]
        print(array)


selection_sort(array)
