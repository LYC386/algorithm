from typing import List


def iterativeBinarySearch(sorted_array: List, target) -> int:
    low = 0
    high = len(sorted_array) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if sorted_array[mid] > target:
            high = mid - 1

        elif sorted_array[mid] < target:
            low = mid + 1

        else:
            return mid

    return -1


def resursiveBinarySearch(sorted_array: List, target, start_index=0) -> int:
    low = 0
    high = len(sorted_array) - 1
    mid = (low + high) // 2
    if len(sorted_array) == 0:
        return -1

    # base_case:
    elif sorted_array[mid] == target:
        return mid + start_index

    elif sorted_array[mid] > target:
        return resursiveBinarySearch(
            sorted_array[:mid], target, start_index=start_index
        )

    elif sorted_array[mid] < target:
        return resursiveBinarySearch(
            sorted_array[mid + 1 :], target, start_index=start_index + mid + 1
        )


if __name__ == "__main__":
    print(iterativeBinarySearch([2, 4, 6, 8, 10, 145], 10))
    print(resursiveBinarySearch([2, 4, 6, 8, 10, 145], -12))
