# Password generator using string modules in python
import string
import random

# string.ascii_lowercase- has all "alphabet" in lowercase
# string.ascii_uppercase- has all "alphabet" in uppercase
# string.digits         - has all "digits" from 0 to 9
# string.punctuation    - has all "symbols"
st_char_lower = string.ascii_lowercase
st_char_upper = string.ascii_uppercase
st_digits = string.digits
st_symbols = string.punctuation
len = int(input("enter the length of your password: "))
emp_St = []

# use extend funtion to add elements in the emp_st
emp_St.extend(list(st_char_lower))
emp_St.extend(list(st_char_upper))
emp_St.extend(list(st_digits))
emp_St.extend(list(st_symbols))
# print(emp_St) - this will print that emp string has all the digits (uppercase and lowercase), digits , symbols

# now shuffle the string
random.shuffle(emp_St)
print("Your generated password is", "".join(emp_St[0:len]))
