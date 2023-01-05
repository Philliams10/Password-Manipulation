import string
import random

# combine all available charaters into a variable
allchar = string.ascii_letters+string.digits+string.punctuation

# take the number given from the user input, convert it to an int and put the int into a variable
len = int(input("Password Length: "))

# print the given statement and new password
print("New Password: " + ''.join(random.sample(allchar, k=len)))