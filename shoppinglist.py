shopping_list =[]

def show_menu():
    print("\n=== SHOPPING LIST MENU ===")
    print("1. Add item")
    print("2. View items")
    print("3. Delete item")
    print("4. Clear List")
    print("5. Exit")

def view_list():
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list,1):
            print(f"{i}. {item}")

def add_item():
    item = input("\nEnter Item Name: ")
    shopping_list.append(item)
    print(f"✅ '{item}' has been added to your shopping list.")

def remove_item():
    view_list()
    if shopping_list:
        try:
            item_number = int(input("\nEnter Item Number that you want to remove: "))
            removed = shopping_list.pop(item_number - 1)
            print(f"❌ '{removed}' has been removed.")
        except ValueError:
            print("⚠️ Invalid input. Please try again.")

def clear_list():
    shopping_list.clear()
    print("🧹 Shopping list cleared.")


while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        view_list()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        clear_list()
    elif choice == "5":
        print("👋 Goodbye! Happy shopping!")
        break
    else:
        print("⚠️ Invalid choice. Please try again.")
