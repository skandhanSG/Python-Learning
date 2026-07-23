import string
import secrets
import random 

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digit = string.digits
punctuations = string.punctuation

all_characters = uppercase + lowercase + digit + punctuations

# Use 'choices' (plural) to accept the 'k' argument
passwords = [secrets.choice(all_characters) for _ in range(10)]

password = [random.choice(all_characters) for _ in range(10)]
# 'secrets.choices' returns a list, so join it into a string
final_password = "".join(passwords)

final_passwords = "".join(password)

print(final_password)
print(final_passwords)