# Head fibonacci
def head_fibonacci(n):
    if n == 0:
        result = 0
        return result
    elif n == 1:
        result = 1
        return result
    else:
        result = head_fibonacci(n - 1) + head_fibonacci(n - 2)
        return result


print(head_fibonacci(7))


# Tail Fibonacci
def tail_fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b

    return tail_fibonacci(n - 1, b, a + b)

print(tail_fibonacci(7))
