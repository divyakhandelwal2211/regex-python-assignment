# try:
#     print("hey")
#     print("abc" + 10)
#     print("hello")
# except:
#     print("error is been handled")


# try:
#     print("hey")
#     print("abc" + 10)
#     print("hello")
# except Exception as e:
#     print("error is been handled", e)


# try:
#     print("hey")
#     10 / 0
#     print("hello")
# except NameError as e:
#     print("error is been handled:", e)
# except ZeroDivisionError as e:
#     print("Zero Error is been handled:", e)


# try:
#     print("hey")
#     10 / 0
#     print("hello")
# except (NameError, ZeroDivisionError) as e:
#     print("error is been handled:", e)


# try:
#     print("hey")
#     try:
#         10 / 0
#     except:
#         print("Divided by zero error handled")
#     print("hello")
# except (NameError, ZeroDivisionError) as e:
#     print("error is been handled:", e)


# try:
#     print("hey")
#     print("hello")
# except:
#     print("error is been handled")
# else:  # if try block don't have any error then else block will execute
#     print("else block")


# try:
#     print("hey")
#     print("hello")
# except:
#     print("error is been handled")
# else:  # if try block don't have any error then else block will execute
#     print("else block")
# finally:                    # always execute
#     print("finally block")


"""generate the exception"""
# try:
#     age = 17
#     if age < 18:
#         raise ValueError
# except ValueError:
#     print("value error due to age")

"""assert"""  # for debugging and testing
# x = 10
# assert x != 10, "hey"


# def divide2(a, b):
#     assert b != 0, "can't divide by zero"
#     return a / b


# x = divide2(10, 2)
# print(x)


# try:
#     with open("file.txt", "r") as f:
#         raise FileNotFoundError
# except FileNotFoundError:
#     print("file not exist")
