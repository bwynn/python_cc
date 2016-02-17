user_name = raw_input("What is your name? ")

def greet_user(name):
    """Display a simple greeting."""
    print("Hello " + name.title() + ".")

greet_user(user_name)
