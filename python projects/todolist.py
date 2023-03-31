#Todolist app

def show_menu():
    print("1. Add item")
    print("2. View list")
    print("3. Edit item")
    print("4. Delete item")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_item(): # adding the item in the list.
    item = input("Enter a new item: ") #input from the user 
    with open("todo.txt", "a") as file:  #appends the item in the text file
        file.write(item + "\n")
    print("Item added.")   #item is added 

def view_list(): #viewing the item in the list
    with open("todo.txt") as file: #opens the text file.
        items = file.readlines()
    if not items:
        print("No items in the list.")
    else:
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item.strip()}")

def edit_item():  #editing the item in the list
    with open("todo.txt") as file:
        items = file.readlines()
    if not items:
        print("No items in the list.")
        return
    view_list()
    choice = int(input("Enter the item number to edit: "))
    new_item = input("Enter the new item: ")
    items[choice - 1] = new_item + "\n"
    with open("todo.txt", "w") as file:
        file.writelines(items)
    print("Item updated.")

def delete_item(): #deleting the items in the list
    with open("todo.txt") as file:
        items = file.readlines()
    if not items:
        print("No items in the list.")
        return
    view_list()
    choice = int(input("Enter the item number to delete: "))
    items.pop(choice - 1)
    with open("todo.txt", "w") as file:
        file.writelines(items)
    print("Item deleted.")

while True:
    choice = show_menu()
    if choice == "1":
        add_item()
    elif choice == "2":
        view_list()
    elif choice == "3":
        edit_item()
    elif choice == "4":
        delete_item()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
