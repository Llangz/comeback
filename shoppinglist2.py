# Make a list to hold our items
shopping_list = []
def show_help():
# print out instructions on how to use the app
    print("What else do you want to add to the cart?")
    print("""
Enter 'DONE' to stop adding items
Enter 'HELP' to seek help
Enter 'SHOW' to see your list
""")
def show_list():
    print("Here's your list!")
    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {} items".format(new_item, len(shopping_list)))
show_help()
#     ask for new item
while True:

    new_item = input(">> ")
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)
#
show_list()
