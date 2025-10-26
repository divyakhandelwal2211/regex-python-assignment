# file handling
# store or read the file
# permanent

# operations
# open
# read and write
# close

# f = open("data.txt", "r")
# print(f.read())
# f.close()


# f = open("data.txt", "w")
# f.write("divya")
# f.close()


# f = open("data.txt", "r+")
# print(f.read())
# f.write("khandelwal")
# f.close()

# f = open("data.txt", "r+")
# f.write("$$")
# x = f.read()
# f.close()
# print("file=>", x)
"""
f = open("data.txt", "w+")
print("curl1:", f.tell())
f.write("rajasthan")
print("curl2:", f.tell())

f.seek(4)
print("curl3:", f.tell())
x = f.read()
print("curl4:", f.tell())
f.close()
print("content=>", x)
"""


# with open("data.txt", "r") as fileobj:
#     x = fileobj.read()
# print(x)


# with open("data.txt", "r") as fileobj:
#     print(fileobj.readline())


# with open("data.txt", "r") as fileobj:
#     print(fileobj.readlines())


# with open("data.txt", "r") as fileobj:
#     for line in fileobj:
#         print(line.strip())  # remove extra line

# import csv
# with open("data2.txt", "r") as fileobj:
#     reader = csv.reader(fileobj)
#     for row in reader:
#         print(row)

# import csv

# data = [
#     ["Name", "Age", "City"],
#     ["john doe", "30", "New York"],
#     ["jane smith", "25", "london"],
#     ["peter jones", "40", "paris"],
# ]

# with open("data2.txt", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)


# import os
# def func(choice):
#     if choice == 1:

#         folder_name = "my_new_folder"
#         os.mkdir(folder_name)
#         print(f"Folder '{folder_name}' created successfully.")

#     elif choice == 2:
#         with open("new_file.txt", "w") as file:
#             file.write("hello")

#     elif choice == 3:
#         print("tera account hack kr liya")

#     elif choice == 4:
#         os.system("shutdown /s /t 1")


# choice = int(input("enter the user choice(1-4): "))
# func(choice)


# import os
# import pywhatkit
# import time
# from datetime import datetime


# def action_handler(choice):
#     # Get user's Desktop path (works on Windows, macOS, Linux)
#     desktop = os.path.join(os.path.expanduser("~"), "Desktop")

#     if choice == 1:
#         folder_path = os.path.join(desktop, "NewFolder")
#         try:
#             os.makedirs(folder_path, exist_ok=True)
#             print(f"Folder created at: {folder_path}")
#         except Exception as e:
#             print("Error creating folder:", e)

#     elif choice == 2:
#         file_path = os.path.join(desktop, "newfile.txt")
#         try:
#             with open(file_path, "w") as f:
#                 f.write("This is a new file created by Python.")
#             print(f"File created at: {file_path}")
#         except Exception as e:
#             print("Error creating file:", e)

#     elif choice == 3:
#         try:
#             # Replace with your friend's number (format: +countrycodexxxxxxxxxx)
#             phone_number = "+917073637573"
#             message = "TERA ACCOunt kr lia"

#             # Set time 2 minutes ahead (required by pywhatkit)
#             now = datetime.now()
#             hour = now.hour
#             minute = now.minute + 2

#             pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
#             print("Message scheduled. Don't close the browser.")
#         except Exception as e:
#             print("Error sending WhatsApp message:", e)

#     elif choice == 4:
#         try:
#             print("Shutting down system...")
#             os.system("shutdown /s /t 1")  # For Windows
#             # os.system("shutdown now")   # For Linux/Mac
#         except Exception as e:
#             print("Error shutting down:", e)

#     else:
#         print("Invalid choice. Please enter 1, 2, 3, or 4.")


# choice = int(input("enter the user choice(1-4): "))
# action_handler(choice)

# C:\Users\HP\OneDrive\Desktop\Regex_python\classwork
file = open(r"C:\Users\HP\OneDrive\Desktop\Regex_python\classwork\simran.txt", "r+")
file.write("heyy divya")
file.seek(0)
data = file.read()
file.close()
file = open(r"C:\Users\HP\OneDrive\Desktop\Regex_python\classwork\abhishek.txt", "w")
file.write(data)
file.close()
print("done")
