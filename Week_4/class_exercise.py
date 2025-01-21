#wrote a program to test the various list related methods
# create empty list
#create menu Option for append remove pop clear 

def main():
    global names
    names = []
    menu_list()

def menu_list():

    menu = input("Welcome, what would you like to do? (lowercase please) ")

    if menu == "append":
        a = input("What would you like to append? ")
        names.append(a)
        print(f"The names in the list are : {names} ")
        cont()

    elif menu == "remove":
        b = input("What would you like to remove? ")
        names.remove(b)
        print(f"The names in the list are : {names} ")
        cont()

    elif menu == "pop":
        c = input("What would you like to pop? ")
        names.pop(c)
        print(f"The names in the list are : {names} ")
        cont()

    elif menu == "clear":
        names.clear()
        print(f"The names in the list are : {names} ")
        cont()
    else:
        print("Please enter a valid option.")
        menu_list()


def cont():
    choice = input("Would you like to continue? ")
    if choice == "yes":
        menu_list()
    elif choice == "no":
        print(f"List is {names}")
    else:
        print("Please enter 'yes' or 'no'")
        cont()



if __name__ == '__main__':
    main()
