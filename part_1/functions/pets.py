#def describe_pet(animal_type, pet_name):
#    print("\nI have a " + animal_type + ".")
#    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('hamster', 'harry')

############### KEYWORD ARGUMENTS
#def describe_pet(animal_type, pet_name):
#    print("\nI have a " + animal_type + ".")
#    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet(animal_type='hamster', pet_name='harry')

############### Default Values
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry')
