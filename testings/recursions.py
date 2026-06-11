num = int(input("Enter a number for factorial: "))

def factorial(n) -> str | int:
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "You can't have factorial of negative numbers."
    elif n >= 1000:
        return "The number should be between 0-999"

    return n * factorial(n-1)

print(factorial(num))