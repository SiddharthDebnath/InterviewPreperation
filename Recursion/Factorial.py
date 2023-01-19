# Two types of recursions: Head and tail recursions.
# Head Recursion:
def head_factorial(n):
    # base_case
    if n == 0:
        return 1

    # Recursion
    result = n*head_factorial(n-1)
    return result

print(head_factorial(4))