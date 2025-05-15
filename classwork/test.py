num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
operator = input("enter operator (+,-,/,*): ")

if operator == "+":
    print("num1 + num2 = ", num1 + num2)
elif operator == "-":
    print("num1 - num2 = ", num1 - num2)
elif operator == "/":
    if num2 > 0:
        print("num1 / num2 = ", num1 / num2)
    else:
        print("divided by 0")
elif operator == "*":
    print("num1 * num2 = ", num1 * num2)
else:
    print("Not a valid operator")
