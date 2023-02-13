# Need a sorted array for the below problem.
def binary_search_recursive(container, item, left, right):
    if left > right:
        return -1
    middle_index = (left + right) // 2

    if container[middle_index] == item:
        return middle_index

    elif container[middle_index] > item:
        print("Checking left portion...")
        return binary_search_recursive(container, item, left, middle_index - 1)

    elif container[middle_index] < item:
        print("Checking right portion...")
        return binary_search_recursive(container, item, middle_index + 1, right)


print(binary_search_recursive([2, 9, 6, 48, 499], 6, 0, 4))


def binary_search_iterative(container, item):
    left = 0
    right = len(container) - 1
    mid = 0

    while left <= right:
        mid = (left + right)/2

# If item is on the right half of the array.
        if container[mid] < item:
            left = mid + 1

# If item is on the left half of the array.
        elif container[mid] > item:
            right = mid - 1

# If item is the middle element.
        else:
            return mid

