# in python 2.+ raw_input required instead of simple input()
# message = raw_input("Type something here: ")
# print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#    message = raw_input(prompt)

#    if message != 'quit':
#        print(message)

################ USING A FLAG
active = True
while active:
    message = raw_input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
