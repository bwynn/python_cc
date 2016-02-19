user_size = raw_input("What size shirt would you like? (Small, Medium, Large) ")
message = raw_input("What would you like your shirt to say? ")

def make_shirt(size, msg):
    print("\nShirt size: " + size.title() + ", Message: " + msg + ".")

make_shirt(user_size, message)
