# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))
# operator = input("enter operator (+,-,/,*): ")

# if operator == "+":
#     print("num1 + num2 = ", num1 + num2)
# elif operator == "-":
#     print("num1 - num2 = ", num1 - num2)
# elif operator == "/":
#     if num2 > 0:
#         print("num1 / num2 = ", num1 / num2)
#     else:
#         print("divided by 0")
# elif operator == "*":
#     print("num1 * num2 = ", num1 * num2)
# else:
#     print("Not a valid operator")


# def find_largest(numbers):
#     maxi = numbers[0]
#     for i in range(1, len(numbers)):
#         if numbers[i] > maxi:
#             maxi = numbers[i]
#     return maxi


# nums = [10, 5, 8, 20, 3]
# largest_num = find_largest(nums)
# print(f"the largest number is {largest_num}")


def is_prime(number):

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


num = 18
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not prime")
