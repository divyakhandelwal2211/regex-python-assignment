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
print("hello")
