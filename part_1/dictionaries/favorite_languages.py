# favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python'
# }

# print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# loop through key,value pairs in object/dictionary
# for name, language in favorite_languages.items():
#    print(name.title() + "'s favorite language is " + language.title() + ".")

################################################################################
# loop through keys in dictionary
# for name in favorite_languages.keys():
#    print(name.title())

################################################################################
# adding in conditional check to return specific values
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#    print(name.title())

#    if name in friends:
#        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

# looping through dictionary keys in order
# for name in sorted(favorite_languages.keys()):
#    print(name.title() + ", thank you for taking the poll.")

################################################################################
# looping through the values
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#    print(language.title())

# use a set() to remove any repetitions in values
# for language in set(favorite_languages.values()):
#    print(language.title())

################################################################################
# Multiple values in a dictionary
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
