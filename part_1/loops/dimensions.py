################################################################################
# Working with TUPLES - an immutable list
dimensions = (200, 50)

# dimensions[0] = 250 -- DOESNT WORK! Tuples are immutable

for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
