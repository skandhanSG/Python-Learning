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


# import string
# import random
# import secrets

# uppercase = string.ascii_uppercase
# lowercase = string.ascii_lowercase
# digit = string.digits
# punctuations = string.punctuation

# password =[]

# random.choice(digit)
# random.choice(uppercase)
# random.choice(lowercase)
# random.choice(punctuations)

# password.append(random.choice(digit))
# password.append(random.choice(uppercase))
# password.append(random.choice(lowercase))
# password.append(random.choice(punctuations))   

# all_characters = uppercase + lowercase + digit + punctuations

# password = "".join(password)

# passwords = []

# LEN =10

# passwords = secrets.choices(all_characters, k=10)

# print(passwords)

# print(password)
