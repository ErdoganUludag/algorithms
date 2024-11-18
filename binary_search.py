array = [1, 1, 5, 6, 3, 9, 2, 6, 2, 4, 8, 261561, 0, 3, 26, 2]
array = sorted(array)


def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid - 1
        elif target > array[mid]:
            left = mid + 1

    return -1


index = binary_search(array, 26)
if index != -1:
    print(index)
