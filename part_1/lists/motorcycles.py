# Arrays - Lists in python
################################################################################
# defining and manipulating arrays
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# change first value
# motorcycles[0] = 'ducati'
# print(motorcycles)

# append (push) to end of list
# motorcycles.append('ducati')
# print(motorcycles)

# insert element by index
# motorcycles.insert(2, 'ducati')
# print(motorcycles)

################################################################################
# removing items
# del motorcycles[0]
# print(motorcycles)

# using the pop method will default to the last item in the list
# popped_motorcycle = motorcycles.pop()
# print(popped_motorcycle)

# last_owned = motorcycles.pop()
# print("The last motorcycle I owned was a " + last_owned.title() + ".")

# pop by index - same as js
# first_owned = motorcycles.pop(0)
# print("The first motorcycle I owned was a " + first_owned.title() + ".")

# remove item by string query/value
# motorcycles.remove('yamaha')
# print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
