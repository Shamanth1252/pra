def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage:
number = 5  # Change this to the number for which you want to find the factorial
print("Factorial of", number, "is", factorial(number))
