# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
# while unprinted_designs:
#    current_design = unprinted_designs.pop()
#    # simulate creating a 3d print of the design
#    print("\nPrinting model: " + current_design)
#    completed_models.append(current_design)

# Display all completed models
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#    print(completed_model)

# make the above code more efficient by placing into two separate functions
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
