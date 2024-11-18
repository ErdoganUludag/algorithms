def merge(array):
    if len(array) > 1:
        mid = len(array) // 2
        leftlist = array[:mid]
        rightlist = array[mid:]
        merge(leftlist)
        merge(rightlist)
        mergeSort(array, leftlist, rightlist)


def mergeSort(array, leftlist, rightlist):
    i = 0
    j = 0
    k = 0

    while len(leftlist) > i and len(rightlist) > j:
        if leftlist[i] > rightlist[j]:
            array[k] = rightlist[j]
            j = j + 1
        else:
            array[k] = leftlist[i]
            i = i + 1
        k = k + 1
    while len(leftlist) > i:
        array[k] = leftlist[i]
        i = i + 1
        k = k + 1
    while len(rightlist) > j:
        array[k] = rightlist[j]
        j = j + 1
        k = k + 1


array = [78, 54, 65, 12, 32, 41, 52, 63, 96, 8, 5, 1, 2, 3, 9, 8, 7, 6, 5, 4]
merge(array)
print(array)
