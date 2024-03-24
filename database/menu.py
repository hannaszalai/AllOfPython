from database import Database
from member import Member


# Main menu
def main_menu(db: Database, options):
    while True:
        # print header
        print_header("Welcome to the Online Book Store")
        # print options
        print_option(options)
        choice = check_choice(len(options))

        # Perform an action based on the user's choice
        if choice == 1:
            Member.member_login(db, options)
        elif choice == 2:
            Member.member_registration(db)
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again")


# Function to print the header
def print_header(title):
    print("\n")
    print("*********************************************************")
    print("***                                                   ***")
    print("***          " + title + "         ***")
    print("***                                                   ***")
    print("*********************************************************")


# Function to print the options
def print_option(options):
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")


# Function to get the user's choice
def check_choice(maxOptions):
    selectoption = None
    while (selectoption is None):
        choice = input("\nType in your option: ")
        try:
            if int(choice) in [x for x in range(1, maxOptions+1)]:
                selectoption = int(choice)
            else:
                print("Invalid option, please try again")
        except Exception:
            selectoption = None
            print("Invalid option, please try again")
    return selectoption
