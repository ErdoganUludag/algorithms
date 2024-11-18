def merge(array):
    print("parçalanan değerler" + str(array))
    length = len(array)
    if length > 1:
        mid = length // 2
        leftlist = array[:mid]
        rightlist = array[mid:]
        merge(leftlist)  # recursion
        merge(rightlist)  # recursion
        mergeSort(array, leftlist, rightlist)


def mergeSort(array, leftlist, rigthlist):
    i = 0
    j = 0
    k = 0
    while i < len(leftlist) and j < len(rigthlist):
        if leftlist[i] < rigthlist[j]:
            array[k] = leftlist[i]
            i = i + 1
        else:
            array[k] = rigthlist[j]
            j = j + 1
        k = k + 1
    while i < len(leftlist):
        array[k] = leftlist[i]
        k = k + 1
        i = i + 1
    while j < len(rigthlist):
        array[k] = rigthlist[j]
        k = k + 1
        j = j + 1
    print("birleştirilmiş hali" + str(array))


unorderedlist = [99, 85, 45, 12, 1, 2, 5, 9, 100, 78, 35, 34, 5, 6, 7]
merge(unorderedlist)
print(unorderedlist)
