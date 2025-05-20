# str1 = "regexian"
# str2 = "tushar"

# count = 0
# for i in str1:
#     if i in str2:
#         count += 1

# print(count)


# def check_palindrome(number):
#     my_dict = {}
#     str_num = str(number)
#     reverse_num = str_num[::-1]
#     if str_num == reverse_num:
#         my_dict["palindrome"] = True
#         return my_dict
#     else:
#         my_dict["palindrome"] = False
#         return my_dict


# number = 12321
# palindrome1 = check_palindrome(number)
# print(palindrome1)


# n = 4
# for i in range(0, n - 1):
#     for j in range(i + 1):
#         if j == 0 or j == i:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range(0, n):
#     for j in range(i, n):
#         if j == i or j == n - 1:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()


# k = 4
# str = "hello hey computer science new"
# # for i in str:
# #     print(i, end=" ")
# #     if len(i) > k:
# #         print(i, end=" ")
# for i in str.split(" "):

#     if len(i) > k:
#         print(i, end=" ")

# str = "ababa"
# mydict = {}
# for i in str:
#     if i not in mydict:
#         mydict[i] = 1
#     else:
#         mydict[i] += 1
# print(mydict)

"""practice"""
# d = {"ravi": 10, "rajnish": 9, "sanjeev": 15}
# mykeys = list(d.keys())
# print(mykeys)
# mykeys.sort()
# print(mykeys)

# dict = {i: d[i] for i in mykeys}
# print(dict)


# d = {2: 56, 1: 2, 5: 12, 4: 24}

# my_list = [i for i in d]
# print(my_list)

# for i in range(len(my_list)):
#     for j in range(0, len(my_list) - i - 1):
#         if my_list[j] > my_list[j + 1]:
#             my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

# print(my_list)
# for i in my_list:
#     print(i, end=" ")

# d = {2: 56, 1: 2, 5: 12, 4: 24}
# for i in sorted(d.keys()):
#     print(i, end=" ")


# country_code = {"India": "0091", "Australia": "0025", "Nepal": "00977"}

# # Set a default value for Japan
# print(country_code.setdefault("Japan", "Not Present"))

# # search dictionary for country code of India
# print(country_code["India"])

# # search dictionary for country code of Japan
# print(country_code["Japan"])


# d = {"a": 100, "b": 200, "c": 300}


# sum = 0
# for i in d.values():
#     sum += i
# print(sum)

# sum1 = sum([i for i in d.values()])
# print(sum1)


# d = {"a": 1, "b": 4, "c": 5, "d": 2}
# my_dict = {}

# for i, j in d.items():
#     if j % 2 == 0:
#         my_dict[i] = j

# print(my_dict)

# marks = {"Ram": 45, "Shyam": 78, "Aman": 52}
# my_dict = {}
# for key in marks:
#     if marks[key] > 50:
#         my_dict[key] = marks[key]

# print(my_dict)


# items = {"pen": 5, "pencil": 12, "eraser": 8}

# my_dict = {}
# for key in items:
#     if items[key] > 10:
#         my_dict[key] = items[key]
#     else:
#         my_dict[key] = 0
# print(my_dict)


# sentence = "this is a test this is only a test"
# # Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}

# my_dict = {}
# for i in sentence.split(" "):
#     if i in my_dict:
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1

# print(my_dict)


# d1 = {"a": 2, "b": 4}
# d2 = {"b": 3, "c": 5}
# # Output: {'a': 2, 'b': 7, 'c': 5}

# result = d1.copy()

# for key in d2:
#     if key in result:
#         result[key] += d2[key]
#     else:
#         result[key] = d2[key]
# print(result)


# sales = {"A": 120, "B": 305, "C": 150}
# #output "B"
# max = "A"

# for key in sales:
#     if sales[key] > sales[max]:
#         max = key
# print(max)


# points = {"p1": 10, "p2": -5, "p3": 0, "p4": -1}
# # Output: {'p1': 10, 'p3': 0}
# for key in points:
#     if points[key] < 0:
#         points.pop(key)
# print(points)

# print("-----------------------------")
# points = {"p1": 10, "p2": -5, "p3": 0, "p4": -1}
# # Output: {'p1': 10, 'p3': 0}
# my_dict = {key: value for key, value in points.items() if value >= 0}
# # for key in points:
# #     if points[key] >= 0:
# #         my_dict[key] = points[key]
# print(my_dict)


# lst = [1, 2, 3, 4]
# # Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
# dict = {}
# for i in lst:
#     if i % 2 == 0:
#         dict[i] = "even"
#     else:
#         dict[i] = "odd"
# print(dict)


# d = {"a": 1, "b": 2, "c": 3}
# # Output: {1: 'a', 2: 'b', 3: 'c'}
# dict = {}
# for key, value in d.items():
#     dict[value] = key
# print(dict)

# Remove duplicates from a list without using set()
# lst = [1, 2, 2, 3, 4, 5, 1, 5]
# remove_duplicate = set(lst)
# print(list(remove_duplicate))


# Find the second largest number in a list
# lst = [1, 3, 6, 5]
# max = lst[0]
# second_max = lst[1]

# for i in lst:
#     if i > max:
#         second_max = max
#         max = i
#     elif i > second_max and i != max:
#         second_max = i
# print(second_max)


# Count even and odd numbers in a list
# lst = [2, 1, 3, 3, 4, 7, 10]
# count_even = 0
# count_odd = 0
# for i in lst:
#     if i % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1

# print("even=>", count_even)
# print("odd=>", count_odd)


# Check if a list is a palindrome
# lst = [1, 2, 3, 2, 1]
# reversed_list = lst[::-1]
# if lst == reversed_list:
#     print("palindrome")
# else:
#     print("not palindrome")


# Sum of elements at even and odd indexes
# lst = [1, 2, 3, 4, 5]
# sum_even = 0
# sum_odd = 0
# for i in range(len(lst)):
#     if i % 2 == 0:
#         sum_even += lst[i]
#     else:
#         sum_odd += lst[i]
# print(sum_even)
# print(sum_odd)


# Count the number of vowels in each word of a sentence and store in dictionary

# str = "i am pursuing data science course"
# my_dict = {}
# for i in str:
#     if i in "aeiou":
#         if i in my_dict:
#             my_dict[i] += 1
#         else:
#             my_dict[i] = 1
# print(my_dict)


# Create a dictionary from two lists: one of keys, one of values
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [5, 4, 3, 2, 1]

# my_dict = {}
# for i in range(len(lst1)):
#     my_dict[lst1[i]] = lst2[i]
# print(my_dict)


# Group words by their starting letter
# Example: ['apple', 'ant', 'banana', 'bat'] → {'a': ['apple', 'ant'], 'b': ['banana', 'bat']}

# lst = ["apple", "ant", "banana", "bat"]
# result = {}

# for word in lst:
#     first_letter = word[0]

#     if first_letter in result:
#         result[first_letter].append(word)
#     else:
#         result[first_letter] = [word]
# print(result)


# Find the elements present in one set but not in another

# Convert a tuple of tuples to a flat list
# Example: ((1, 2), (3, 4)) → [1, 2, 3, 4]


# tuple_of_tuples = (1, (1, 2), 2, (3, 4))
# flat_list = []

# for i in tuple_of_tuples:
#     if type(i) == tuple:
#         flat_list.extend(i)
#     else:
#         flat_list.append(i)
# print(flat_list)
