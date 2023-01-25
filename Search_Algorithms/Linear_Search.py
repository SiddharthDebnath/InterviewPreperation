def linear_search(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i

    return -1


num = [1, 67, 38, 83, 43]
value = 38

print(linear_search(num, value))
