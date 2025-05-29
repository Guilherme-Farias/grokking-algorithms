from typing import List


def binary_search(arr: List[int], target: int) -> int | None:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid

        if guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return None
