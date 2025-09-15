#==========================================================
# I am writing a code, that will create a Passwor Generator.
#===========================================================
import random
import string

print("🔐 Password Generator 🔐")

# Step 1: Ask user for length
length = int(input("Enter the desired password length: "))

# Step 2: Define characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Step 4: Display password
print("\n✅ Your Generated Password is:")
print(password)