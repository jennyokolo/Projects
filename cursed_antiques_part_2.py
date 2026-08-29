print("Welcome to The Cursed Antique Shop!")

cursed_antiques = [
    "Talisman",
    "Monkeys Paw",
    "Cursed Mirror",
    "Haunted Painting",
    "Voodoo Doll",
    "Crystal Ball",
    "Cursed Locket",
    "Ancient Amulet",
    "Phantom Clock",
    "Dorian Gray's Portrait",
    "Cursed Ring",
]

shopping_cart = [
    "Phantom Clock",
]

user_quit = False

# DO NOT CHANGE THE CODE ABOVE HERE
# YOUR CODE BELOW HERE
while not user_quit:
    option = input(
        "What would you like to do?\n" 
        "- Buy an item (enter 'buy')\n" 
        "- Remove antique from shopping cart (enter 'remove')\n" 
        "- Sort antiques (enter 'sort')\n" 
        "- List items (enter 'list')\n" 
        "- Quit (enter 'quit')\n"
        "Option: "
    )

    if option == "quit":
        print("Thank you for visiting the Cursed Antiques Shop!")
        user_quit = True

    elif option == "buy":
        method = input("Would you like to buy the antique by name or index? (Enter 'name' or 'index') ")

        if method == "name":
            item = input("Which item would you like to buy? ")
            if item in cursed_antiques:
                cursed_antiques.remove(item)
                shopping_cart.append(item)
                print(f"{item} was removed from the inventory and added to the shopping cart.")
            else:
                print("That item is not available.")
        
        elif method == "index":
            index_str = input("Which item would you like to buy? ")

            try:
                index = int(index_str)
                if index >= 1 and index <= len(cursed_antiques):
                    item = cursed_antiques.pop(index-1)
                    shopping_cart.append(item)
                    print (f"{item} was removed from the inventory and added to the shopping cart")
                else:
                    print("The item is not available")
            except ValueError:
                print("That item is not available")

    elif option == "sort":
        choice = input("Would you like to sort the antiques in reverse alphbetical order (y/n)? ").lower()
        if choice == "y":
            cursed_antiques.sort(reverse=True)
            print("Antiques sorts in reverse alphabetical order")
        elif choice == "n":
            cursed_antiques.sort()
            print("Antiques sorted in alphabetical order")
        else:
            print("Sorry I didn't understand that")

    elif option == "list":
        choice = input("Would you like to view your shopping cart or available antiques (s/a)? ").lower()
        if choice == "s":
            for i, item in enumerate(shopping_cart, start=1):
                print(f"{i}. {item}")
        elif choice == "a":
            for i, item in enumerate(cursed_antiques, start=1):
                print(f"{i}. {item}")
        else:
            print("Sorry I didn't understand that")
            
    elif option == "remove":
        item = input("Which item would you like to remove from your shopping cart? ")
        try:
            shopping_cart.remove(item)
            cursed_antiques.append(item)
            print(f"{item} was removed from the shopping cart")
        except ValueError:
            print(f"{item} is not in the shopping cart")
    else:
        print("Sorry I didn't understand that. Try again")

