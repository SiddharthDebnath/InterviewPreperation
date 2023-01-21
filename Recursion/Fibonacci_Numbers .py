# Head fibonacci
def head_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib1 = head_fibonacci(n-1)
    fib2 = head_fibonacci(n-2)

    result = fib1 + fib2

    return result

# Tail Fibonacci
def tail_fibonacci(s):
    if s == 0:
        return 0