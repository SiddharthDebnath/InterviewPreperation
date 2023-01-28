# Need a sorted array for the below problem.
def binary_search_recursive(container, item, left, right):
    if left > right:
        return -1
    middle_index = (left+right)//2

    if container[middle_index] == item:
        return middle_index

    elif container[middle_index] > item:
        print("Checking left portion...")
        return binary_search_recursive(container, item, left, middle_index - 1)

    elif container[middle_index] < item:
        print("Checking right portion...")
        return binary_search_recursive(container, item, middle_index + 1, right)


print(binary_search_recursive([2, 9, 6, 48, 499], 6, 0, 4))

