def factorial(a):
    number = a
    incremental = 1
    ans = number

    while incremental < number:

        next_factorial = number - incremental

        ans = ans * next_factorial

        incremental += 1
    return (f"ans: {ans}")

print(factorial(5))