# A movie theater charges different prices depending on a person's age. If a
# person is under the age of 3, the ticket is free; if they are between 3 & 12
# the ticket is $10; if they are over 12, the ticket is 15. Write a loop in which
# you ask the user their age, and tell them the cost of their movie ticket
ticket = {'baby': 0, 'child': 10, 'adult': 15}

age = raw_input("How old are you? ")
age = int(age)

while age:
    if age < 3:
        print("Your movie ticket will be $" + str(ticket['baby']))
        break
    elif age < 12:
        print("Your movie ticket will be $" + str(ticket['child']))
        break
    elif age >= 12:
        print("Your movie ticket will be $" + str(ticket['adult']))
        break
