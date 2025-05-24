# file handling
# store or read the file
# permanent

# operations
# open
# reand and write
# close

# f = open("data.txt", "r")
# print(f.read())
# f.close()


# f = open("data.txt", "w")
# f.write("divya")
# f.close()


f = open("data.txt", "r+")
print(f.read())
f.write("khandelwal")
f.close()
