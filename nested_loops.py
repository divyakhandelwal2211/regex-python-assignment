# for i in range(1, 5):
#     print("---student", i)
#     for j in range(i, 5):
#         print("subject", j)


# for i in range(1, 5):
#     print("---student", i)
#     for j in range(1, 6 - i):
#         print("subject", j)


# for i in range(10, 15):
#     print("---student", i)
#     for j in range(1, 5):
# print("subject", j)

# x = 0
# for i in range(10, 14):
#     print("---student", i)
#     for j in range(1, 7 - x):
#         print("subject", j)
#     x += 2

"""table of 3"""
# num = 3
# for i in range(1, 11):
#     print(f"{num} * {i} = {num*i}")


"""table for 2 ,3 and 4 simultaneously"""
# for num in range(2, 5):
#     for i in range(1, 11):
#         print(f"{num} * {i} = {num*i}")

"""factors"""
# num = int(input("enter a number: "))
# for i in range(2, num + 1):
#     if num % i == 0:
#         print(i)

"""print factors of number from 2 to 20"""
# for num in range(2, 21):
#     for i in range(1, num + 1):
#         if num % i == 0:
#             print(i)
#     print("-----")

"""check a number is prime or not"""
# num = int(input("enter the number: "))
# prime = 0

# for i in range(2, num):
#     if num % i == 0:
#         prime = 1
#         break

# if prime == 0:
#     print("prime")
# else:
#     print("not prime")

"""find prime upto 1 to n"""
# for num in range(3, 41):
#     prime = 0
#     for i in range(2, num):
#         if num % i == 0:
#             prime = 1
#             break

#     if prime == 0:
#         print(num, end=" ")

""" armstrong"""
# for num in range(153, 400):
#     a = num

#     total = 0
#     while num > 0:
#         rem = num % 10
#         num = num // 10
#         total = total + rem**3

#     if total == a:
#         print("armstrong", a)

"""pattern 1"""
# for i in range(1, 5):
#     for j in range(1, 4):
#         print("*", end=" ")
#     print("")


"""pattern 2"""
# for i in range(1, 4):
#     for j in range(1, 5):
#         print(i, end=" ")
#     print("")


"""pattern 3"""
# for i in range(1, 6):
#     for j in range(1, 5):
#         print(j, end=" ")
#     print("")


"""pattern 4"""
# temp = 1
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(temp, end=" ")
#         temp += 1
#     print("")


"""pattern 6"""

# for i in range(8, 4, -1):
#     for j in range(1, 4):
#         print(i, end=" ")

#     print("")


"""pattern 5"""

# for i in range(1, 4):
#     for j in range(65, 68):
#         print(chr(j), end=" ")

#     print("")


"""pattern 7"""

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print("*", end=" ")

#     print("")

"""1
23
456
78910"""
# temp = 1
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(temp, end=" ")
#         temp += 1
#     print("")

"""8
77
666
5555"""
# temp = 8
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(temp, end=" ")
#     temp -= 1
#     print("")


"""1
10
101
1010"""

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         if j % 2 != 0:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print("")

"""* * * * 
* * * 
* *
*"""
# for i in range(1, 5):
#     for j in range(5, i, -1):
#         print("*", end=" ")
#     print("")

"""- - - * 
   - - * * 
   - * * * 
   * * * *"""
# for i in range(1, 5):
#     for j in range(i, 4):
#         print("-", end=" ")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print("")

"""A 
   A B 
   A B C
   A B C D
   A B C D E"""

# for i in range(1, 6):
#     for j in range(i):
#         print(chr(65 + j), end=" ")

#     print("")

"""A 
B B 
C C C
D D D D
E E E E E"""

# for i in range(5):
#     for j in range(1, i + 2):
#         print(chr(65 + i), end=" ")

#     print("")

"""       * 
        * * 
      * * *
    * * * *
  * * * * *"""

# for i in range(1, 6):
#     for j in range(i, 6):
#         print(" ", end=" ")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print("")

"""       1 
        1 2 
      1 2 3
    1 2 3 4
  1 2 3 4 5"""
# for i in range(1, 6):
#     for j in range(i, 6):
#         print(" ", end=" ")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print("")

"""1 2 3 4 5 
     1 2 3 4 
       1 2 3
         1 2
           1"""
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(" ", end=" ")
#     for j in range(1, 7 - i):
#         print(j, end=" ")
#     print()

""" A B C D E 
      A B C D 
        A B C
          A B
            A"""
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(" ", end=" ")
#     for j in range(0, 6 - i):
#         print(chr(65 + j), end=" ")
#     print()

"""  * * * * * 
    * * * * *
   * * * * *
  * * * * *
 * * * * *"""
# for i in range(1, 6):
#     for j in range(i, 6):
#         print(" ", end="")
#     for j in range(1, 6):
#         print("*", end=" ")
#     print("")

"""  1 2 3 4 5 
    1 2 3 4 5
   1 2 3 4 5
  1 2 3 4 5
 1 2 3 4 5"""
# for i in range(1, 6):
#     for j in range(i, 6):
#         print(" ", end="")
#     for j in range(1, 6):
#         print(j, end=" ")
#     print("")


"""  A B C D E
    A B C D E
   A B C D E
  A B C D E
 A B C D E"""
# for i in range(1, 6):
#     for j in range(i, 6):
#         print(" ", end="")
#     for j in range(5):
#         print(chr(65 + j), end=" ")
#     print("")

"""****
    ****
     ****
      ****"""
# for i in range(1, 5):
#     for j in range(1, i):
#         print(" ", end="")
#     for j in range(1, 5):
#         print("*", end="")
#     print()
