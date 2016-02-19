f_name = raw_input("What's the musican's first name? ")
m_name = raw_input("What's the musician's middle name? Leave empty if none specified ")
l_name = raw_input("What's the musician's last name? ")

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name(f_name, l_name, m_name)
print(musician + " is a great musician.")
