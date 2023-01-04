print('Welcome to the..')
print('''
╔═╗┌─┐┌─┐┌─┐╦ ╦┌─┐┬─┐┌┬┐  ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐┬
╠═╝├─┤└─┐└─┐║║║│ │├┬┘ ││  ║ ╦├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘│
╩  ┴ ┴└─┘└─┘╚╩╝└─┘┴└──┴┘  ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─o 
''')
import random

letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k',
           'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v',
           'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_of_letters = int(input("How many characters needed for your password?\n "))
num_of_numbers = int(input(f"How many numbers would like in your password?\n"))
num_of_symbols = int(input(f"How many symbols would you like in your password?\n"))

password = ""
for char in range(1, num_of_letters + 1):
    password += random.choice(letters)

for char in range(1, num_of_numbers + 1):
    password += random.choice(numbers)

for char in range(1, num_of_symbols + 1):
    password += random.choice(symbols)

print(password)

strong_password = []
for char in range(1, num_of_letters + 1):
    strong_password.append(random.choice(letters))

for char in range(1, num_of_numbers + 1):
    strong_password.append(random.choice(numbers))

for char in range(1, num_of_symbols + 1):
    strong_password.append(random.choice(symbols))

print(strong_password)
random.shuffle(strong_password)
print(strong_password)

new_password = ""
for char in strong_password:
    new_password += char

print(f"Your new generated password is: {new_password}")

