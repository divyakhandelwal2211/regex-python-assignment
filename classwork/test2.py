# my_dict = {"A": 1, "B": 2}

# a = my_dict["A"]
# print(a)
# my_dict["B"] = a

# print(my_dict)


lst = [2, 4, 3, 1, 5]

mini = lst[0]
sec_min = lst[1]

for i in range(2, len(lst)):
    if lst[i] < min:
        sec_min = min
        min = lst[i]

    elif lst[i] < sec_min and lst[i] != min:
        sec_min = lst[i]

print(sec_min)
