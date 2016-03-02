filename = 'pi_long.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = raw_input("Enter your birthday, in the form of mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first huge number of digits less than one million of pi!")
else:
    print("Your birthday is not special enough to be included in pi. That makes you a square!")
