prompt = "\nPlease enter the name of a city that you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = raw_input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
