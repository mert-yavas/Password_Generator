import random

# Define the possible characters for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Greeting message for the user
print("Welcome to the PyPassword Generator!")

# Asking the user for their preferences
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Initialize an empty list to store the password elements
password = []

# Adding random letters to the password
for i in range(nr_letters):
    password.append(random.choice(letters))

# Adding random symbols to the password
for i in range(nr_symbols):
    password.append(random.choice(symbols))

# Adding random numbers to the password
for i in range(nr_numbers):
    password.append(random.choice(numbers))

# Shuffling the password to ensure randomness
random.shuffle(password)

# Converting the list of characters into a single string
shuffled_password_no_comma = "".join(password)

# Display the final password to the user
print(f"Your password is: {shuffled_password_no_comma}")
