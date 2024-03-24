from database import Database  # book_store database connection
from getpass import getpass  # Hide password input
from mysql.connector import connect  # MySQL connection
from menu import main_menu  # Main menu


# Login to the database
def check_credentials(username, password):
    try:
        connect(host="localhost", user=username,
                password=password, database="book_store")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


valid_connection = False
user, password = (None, None)


while (not valid_connection):
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    if (check_credentials(username, password)):
        valid_connection = True
    else:
        print("Invalid credentials. Try again")

db = Database(username, password)
options = ["Member Login", "New Member Registration", "Exit"]
main_menu(db, options)
