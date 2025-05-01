"""print prime nummber from 1 to n here n is user input"""

# num = int(input("enter the number: "))
# for i in range(2, num + 1):
#     prime = 0
#     for j in range(2, i):
#         if i % j == 0:
#             prime = 1
#             break
#     if prime == 0:
#         print(i, end=" ")


"""wap to find factorial"""

# num = int(input("enter the number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial = factorial * i
# print("factorial = ", factorial)


"""wap to find prime factors"""

# num = int(input("enter the number: "))

# i = 2
# while num > 1:
#     if num % i == 0:
#         print(i, end=" ")
#         num //= i
#     else:
#         i += 1


"""wap to find lcm of two number"""

# num1 = int(input("enter the number1: "))
# num2 = int(input("enter the number2: "))

# if num1 > num2:
#     max = num1
# else:
#     max = num2

# while True:
#     if max % num1 == 0 and max % num2 == 0:
#         lcm = max
#         break
#     else:
#         max += 1

# print("lcm - ", lcm)


"""wap to check number is armstrong or not"""

# num = int(input("Enter the number: "))
# temp = num

# total_count = len(str(num))

# total = 0
# while int(num) > 0:
#     digit = num % 10
#     total += digit**total_count
#     num //= 10


# if total == temp:
#     print("armstrong")
# else:
#     print("not armstrong")

"""19.Write a program to check whether a number is Strong number or not
a. Strong number is a special number whose sum of factorial digits is
equal to the original number."""

# num = int(input("Enter the number: "))

# temp = num
# total = 0
# while num > 0:
#     digit = num % 10

#     factorial = 1
#     for i in range(1, digit + 1):
#         factorial *= i

#     total += factorial
#     num //= 10

# if total == temp:
#     print("strong number")
# else:
#     print("not strong number")


"""wap to check the number is perfect or not"""

# num = int(input("Enter the number: "))
# temp = num
# total = 0
# for i in range(1, num):
#     if num % i == 0:
#         total += i

# if total == temp:
#     print("perfect number")
# else:
#     print("not a perfect number")


"""wap of fibonacci series"""
# num = int(input("enter the number of terms: "))
# a = 0
# b = 1
# for i in range(num):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c


"""wap to find ones complement of a number"""
binary = input("enter the number in binary: ")
ones_complement = ""
for i in binary:
    if i == "1":
        ones_complement += "0"
    else:
        ones_complement += "1"
print(ones_complement)
