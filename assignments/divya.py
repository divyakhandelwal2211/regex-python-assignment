def fact(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
        return factorial


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def check_palindrome(n):
    original = n
    number = 0
    digit = n % 10
    number = number * 10 + digit
    n = n // 10

    if original == number:
        print("palindrom")
    else:
        print("not palindrom")
