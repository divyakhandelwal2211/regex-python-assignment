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

num1 = int(input("enter the number1: "))
num2 = int(input("enter the number2: "))

if num1 > num2:
    max = num1
else:
    max = num2

while True:
    if max % num1 == 0 and max % num2 == 0:
        lcm = max
        break
    else:
        max += 1

print("lcm - ", lcm)
