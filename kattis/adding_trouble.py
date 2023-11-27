"""Kattis Problem"""

user_input = input("")
user_input_splitted = user_input.split(" ")

if int(user_input_splitted[0]) + int(user_input_splitted[1]) == int(user_input_splitted[2]):
    print("correct!")
else:
    print("wrong!")