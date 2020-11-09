#Password Generator Project
from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 

nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

print("")

password_list = []

# Auto generatingpassword letters:
pass_letters = ""
for l in range(nr_letters):
  password_list.append(choice(letters))

# Auto generating password symbols:
pass_symbols = ""
for s in range(nr_symbols):
  password_list.append(choice(symbols)) 

# Auto generating password numbers:
pass_num = ""
for num in range(nr_numbers):
  password_list.append(choice(numbers))

print("")
shuffle(password_list)
# assembled_pass = pass_letters + pass_num + pass_symbols
auto_password =  "".join(password_list) 
print(f"your auto-generated password is: {auto_password}")