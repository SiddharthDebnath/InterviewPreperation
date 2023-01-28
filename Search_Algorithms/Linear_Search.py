def linear_search(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i

    return -1


num = [1, 67, 38, 83, 43]
value = 38

print(linear_search(num, value))


def linear_search_recursive(container, item, index=0):
    if index >= len(container):
        return -1

        # base case when we find the item
    if container[index] == item:
        return index

    return linear_search_recursive(container, item, index + 1)


nums = [1, 4, 6, -4, 0, 100]
print(linear_search_recursive(nums, 0))
