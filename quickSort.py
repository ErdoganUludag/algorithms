def quick(array, leftindex, rightindex):
    i = leftindex - 1
    pivot = array[rightindex]

    for j in range(leftindex, rightindex):
        if array[j] < array[rightindex]:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[rightindex] = array[rightindex], array[i + 1]
    return i + 1


def quicksort(array, leftindex, rightindex):
    if leftindex < rightindex:
        pivot = quick(array, leftindex, rightindex)
        quicksort(array, leftindex, pivot - 1)
        quicksort(array, pivot + 1, rightindex)


unorderedlist = [96, 36, 25, 14, 75, 85, 45, 69, 56, 21, 78, 16, 68]
quicksort(unorderedlist, 0, len(unorderedlist) - 1)
print(unorderedlist)
