import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_rand_list = []

for letter in range(0, nr_letters):
    element = random.choice(letters)
    password_rand_list.append(element)

for symbol in range(0, nr_symbols):
    element = random.choice(symbols)
    password_rand_list.append(element)

for number in range(0, nr_numbers):
    element = random.choice(numbers)
    password_rand_list.append(element)

print(password_rand_list)
random.shuffle(password_rand_list)
print(password_rand_list)

# password = texto = ''.join(map(str, password_rand_list))
# print(password)

password = ''

for char in password_rand_list:
    password += char

print(f"Your password is: {password}")
