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

"""   *
     ***
    *****
   *******"""

# for i in range(1, 5):
#     for j in range(i, 4):
#         print(" ", end="")
#     for j in range(1, i):
#         print("*", end="")
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()


"""   *
     * *
    *   *
   *******"""
# for i in range(1, 5):
#     for j in range(i, 4):
#         print(" ", end="")
#     for j in range(1, i):
#         if j == 1 or i == 4:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     for j in range(1, i + 1):
#         if i == 4 or i == 1 or i == j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


""" *******
     *****
      ***
       *"""
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(" ", end="")
#     for j in range(i, 4):
#         print("*", end="")
#     for j in range(i, 5):
#         print("*", end="")
#     print()

"""*
   **
   ***
   ****
   ***
   **
   *"""
# for i in range(1, 4):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()
# for i in range(1, 5):
#     for j in range(i, 5):
#         print("*", end="")
#     print()


""" *
   **
  ***
 ****
  ***
   **
    *"""
# for i in range(1, 4):
#     for j in range(i, 5):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(" ", end="")
#     for j in range(i, 5):
#         print("*", end="")
#     print()

"""*
  ***
 *****
*******
 *****
  ***
   *"""
# for i in range(1, 4):
#     for j in range(i, 4):
#         print(" ", end="")
#     for j in range(1, i):
#         print("*", end="")
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()
# for i in range(1, 5):
#     for j in range(1, i):
#         print(" ", end="")
#     for j in range(i, 4):
#         print("*", end="")
#     for j in range(i, 5):
#         print("*", end="")
#     print()

""" 1
   12
  123
 1234
12345"""
# for i in range(1, 6):
#     p = 1
#     for j in range(1, i + 1):
#         print(p, end="")
#         p += 1
#     print()

"""12345
   1234
   123
   12
   1"""
# for i in range(1, 6):
#     p = 1
#     for j in range(i, 6):
#         print(p, end="")
#         p += 1
#     print()

"""1 
   1 2 
   1   3
   1     4
   1 2 3 4 5"""
# for i in range(1, 6):
#     p = 1
#     for j in range(1, i + 1):
#         if j == 1 or i == 5 or i == j:
#             print(p, end=" ")
#         else:
#             print(" ", end=" ")
#         p += 1
#     print()

""" 1 
   1 2 
  1   3 
 1     4 
1 2 3 4 5 """
# for i in range(1, 6):
#     for j in range(i, 5):
#         print(" ", end="")
#     p = 1
#     for j in range(1, i + 1):
#         if j == 1 or i == 5 or i == j:
#             print(p, end=" ")
#         else:
#             print(" ", end=" ")
#         p += 1
#     print()


"""     * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * *
        *"""
# for i in range(1, 5):
#     for j in range(i, 5):
#         print(" ", end=" ")
#     for j in range(1, i):
#         print("*", end=" ")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(1, i):
#         print(" ", end=" ")
#     for j in range(i, 5):
#         print("*", end=" ")
#     for j in range(i, 6):
#         print("*", end=" ")
#     print()

"""     1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1"""
# for i in range(1, 5):
#     for j in range(i, 5):
#         print(" ", end=" ")
#     p = 1
#     for j in range(1, 2 * i):
#         print(p, end=" ")
#         p += 1
#     print()

# for i in range(5, 0, -1):
#     for j in range(5, i, -1):
#         print(" ", end=" ")
#     for j in range(1, 2 * i):
#         print(j, end=" ")
#     print()

"""1 2 3 4 5 6 7 8 9 
    1 2 3 4 5 6 7 
      1 2 3 4 5
        1 2 3
          1
        1 2 3
      1 2 3 4 5
    1 2 3 4 5 6 7
  1 2 3 4 5 6 7 8 9"""
# for i in range(5, 1, -1):
#     for j in range(5, i, -1):
#         print(" ", end=" ")
#     for j in range(1, 2 * i):
#         print(j, end=" ")
#     print()
# for i in range(1, 6):
#     for j in range(i, 5):
#         print(" ", end=" ")
#     for j in range(1, 2 * i):
#         print(j, end=" ")
#     print()

"""A B C D E F G H I 
    A B C D E F G
      A B C D E
        A B C
          A
        A B C
      A B C D E
    A B C D E F G
  A B C D E F G H I"""
# for i in range(5, 1, -1):
#     for j in range(5, i, -1):
#         print(" ", end=" ")
#     p = 65
#     for j in range(1, 2 * i):
#         print(chr(p), end=" ")
#         p += 1
#     print()
# for i in range(1, 6):
#     for j in range(i, 5):
#         print(" ", end=" ")
#     p = 65
#     for j in range(1, 2 * i):
#         print(chr(p), end=" ")
#         p += 1
#     print()

""" * * * * * 
    *       * 
    *       *
    *       *
    * * * * *"""
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or j == 1 or j == 5 or i == 5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")

#     print()

""" 1 2 3 4 5 
    1       5 
    1       5
    1       5
    1 2 3 4 5"""
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or j == 1 or j == 5 or i == 5:
#             print(j, end=" ")
#         else:
#             print(" ", end=" ")

#     print()

""" A B C D E 
    A       E 
    A       E
    A       E
    A B C D E"""
# for i in range(1, 6):
#     p = 65
#     for j in range(1, 6):
#         if i == 1 or j == 1 or j == 5 or i == 5:
#             print(chr(p), end=" ")
#         else:
#             print(" ", end=" ")
#         p += 1
# print()

"""     * 
      *   * 
    *       * 
  *           * 
*               *      
  *           *        
    *       *
      *   *
        *       """
# for i in range(1, 5):
#     for j in range(i, 5):
#         print(" ", end=" ")
#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# for i in range(5, 0, -1):
#     for j in range(5, i, -1):
#         print(" ", end=" ")
#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

"""     A 
      A   C 
    A       E
  A           G        
A               I      
  A           G        
    A       E
      A   C
        A         """
# for i in range(1, 5):
#     for j in range(i, 5):
#         print(" ", end=" ")
#     p = 65
#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print(chr(p), end=" ")
#         else:
#             print(" ", end=" ")
#         p += 1
#     print()

# for i in range(5, 0, -1):
#     for j in range(5, i, -1):
#         print(" ", end=" ")
#     p = 65
#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print(chr(p), end=" ")
#         else:
#             print(" ", end=" ")
#         p += 1
#     print()

"""******
   *    *
   *    *
   ******"""
# for i in range(1, 5):
#     for j in range(1, 7):
#         if i == 1 or i == 4 or j == 1 or j == 6:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


""" *        *
    **      **
    ***    ***
    ****  ****
    **********
    ****  ****
    ***    ***
    **      **
    *        *"""
# for i in range(5, 0, -1):
#     for j in range(5, i - 1, -1):
#         print("*", end="")
#     for j in range(1, 2 * i - 1):
#         print(" ", end="")
#     for j in range(5, i - 1, -1):
#         print("*", end="")
#     print()
# for i in range(1, 5):
#     for j in range(i, 5):
#         print("*", end="")
#     for j in range(1, 2 * i + 1):
#         print(" ", end="")
#     for j in range(i, 5):
#         print("*", end="")
#     print()


""" ***** *****
    ****   ****
    ***     ***
    **       **
    *         *
    *         *
    **       **
    ***     ***
    ****   ****
    ***** *****"""
# for i in range(1, 6):
#     for j in range(i, 6):
#         print("*", end="")
#     for j in range(1, 2 * i):
#         print(" ", end="")
#     for j in range(i, 6):
#         print("*", end="")
#     print()

# for i in range(5, 0, -1):
#     for j in range(5, i - 1, -1):
#         print("*", end="")
#     for j in range(1, 2 * i):
#         print(" ", end="")
#     for j in range(5, i - 1, -1):
#         print("*", end="")
#     print()


"""       1 
        2 3 2 
      3 4 5 4 3
    4 5 6 7 6 5 4
  5 6 7 8 9 8 7 6 5"""
# n = 5
# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         print(" ", end=" ")
#     num = i
#     for j in range(1, i + 1):
#         print(num, end=" ")
#         num += 1
#     num -= 2
#     for j in range(1, i):
#         print(num, end=" ")
#         num -= 1
#     print()


# for i in range(1, 6):
#     for j in range(i, 6):
#         if i == 5 or j == i or i == 1:
#             print(j, end=" ")
#         else:
#             print(" ", end=" ")
#     print()

""" E 
    D E
    C D E
    B C D E
    A B C D E"""
# for i in range(1, 6):
#     x = 70 - i
#     for j in range(i):
#         print(chr(x + j), end=" ")
#     print()


""" 1 2 3 4 5 
    2     5 
    3   5
    4 5
    5"""
# for i in range(1, 6):
#     for j in range(i, 6):
#         if i == 1 or j == i or j == 5:
#             print(j, end=" ")
#         else:
#             print(" ", end=" ")
#     print()
