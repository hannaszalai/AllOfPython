import datetime


class Member:
    # Option 2: New member registration
    def __init__(self, fname, lname, address, city,
                 zip, phone, email, password):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.city = city
        self.zip = zip
        self.phone = phone
        self.email = email
        self.password = password

    # This method prints the header for the member registration.
    @staticmethod
    def member_header():
        print("\nWelcome to the Online Book Store")
        print("\tNew Member Registration")

    # This method handles the member registration process.
    @staticmethod
    def member_registration(db):
        Member.member_header()
        first_name = input("\nEnter first name: ")
        last_name = input("Enter last name: ")
        street_address = input("Enter street address: ")
        city = input("Enter city: ")
        zip_code = input("Enter zip: ")
        phone = input("Enter phone: ")
        email = input("Enter email address: ")
        password = input("Password: ")

        # Create a new member with the provided details
        new_member = Member(first_name, last_name, street_address,
                            city, zip_code, phone, email, password)

        # Insert the new member into the database
        query = (
            f"INSERT INTO members (fname, lname, address, "
            f"city, zip, phone, email, password) "
            f"VALUES ('{new_member.fname}', '{new_member.lname}', "
            f"'{new_member.address}', '{new_member.city}', "
            f"'{new_member.zip}', '{new_member.phone}', "
            f"'{new_member.email}', '{new_member.password}')"
        )

        db.execute_with_commit(query)

        print("You have registered successfully!")
        input("Press Enter to go back to Menu")

    # Option 1: Member Login
    @staticmethod
    def member_login_header():
        print("*********************************************************")
        print("***                                                   ***")
        print("***          Welcome to the Online Book Store         ***")
        print("***                  Member Menu                      ***")
        print("***                                                   ***")
        print("*********************************************************")

    # This method handles the member login process.
    @staticmethod
    def member_login(db, m_options):
        email = input("Enter email: ")
        password = input("Enter password: ")
        print("\n")

        # Fetch password from the database based on the provided email
        query = f"SELECT password FROM members WHERE email = '{email}'"
        result = db.execute_with_fetchall(query)

        if result:
            stored_password = result[0][0]
            if password == stored_password:
                print("Login successful!")
                # Fetch userid from the database based on the provided email
                query = f"SELECT userid FROM members WHERE email = '{email}'"
                userid = db.execute_with_fetchall(query)[0][0]

                # Create a Member object with the userid
                member = Member(None, None, None, None, None,
                                None, email, password)
                member.userid = userid
                Member.member_menu(db, member)
                print("\n")
            else:
                print("Invalid password. Login failed.")
        if result:
            stored_password = result[0][0]
            if password == stored_password:
                print("Login successful!")
                # Fetch user details based on the provided email
                query_user_details = (
                    f"SELECT userid, fname, lname "
                    f"FROM members WHERE email = '{email}'"
                )
                user_details = db.execute_with_fetchall(query_user_details)

                if user_details:
                    userid, fname, lname = user_details[0]
                    # Update the member object with user details
                    member.userid = userid
                    member.fname = fname
                    member.lname = lname

                    Member.member_menu(db, member)
                    print("\n")
                else:
                    print("Error: Failed to retrieve user details.")
            else:
                print("Invalid password. Login failed.")
        else:
            print("User not found. Login failed.")

    # This method checks if the provided choice is valid.
    @staticmethod
    def member_check_choice(maxOptions):
        selectoption = None
        while (selectoption is None):
            print("\n")
            m_choice = input("Type in your option: ")
            try:
                if int(m_choice) in [x for x in range(1, maxOptions+1)]:
                    selectoption = int(m_choice)
                else:
                    print("Invalid option, please try again")
            except Exception:
                selectoption = None
                print("Invalid option, please try again")
        return selectoption

    # This method handles the member menu.
    @staticmethod
    def member_menu(db, member):
        Member.member_login_header()
        print("1. Browse by Subject")
        print("2. Search by Author/Title")
        print("3. Check Out")
        print("4. Logout")
        # Collect user input for the menu choice
        choice = Member.member_check_choice(4)

        # Execute the corresponding action based on the choice
        if choice == 1:
            Member.browse_by_subject(db, member)
        elif choice == 2:
            Member.search_by_author_title(db, member)
        elif choice == 3:
            Member.check_out(db, member)
        elif choice == 4:
            print("Logging out...")
        else:
            print("Invalid option, please try again")

    # Member menu - Option 1: Browse by Subject
    @staticmethod
    def browse_by_subject(db, member):
        # Fetch all subjects from the database
        subjects = db.execute_with_fetchall(
            "SELECT DISTINCT subject FROM books ORDER BY subject"
        )

        # Display all subjects
        for i, subject in enumerate(subjects, 1):
            print(f"{i}. {subject[0]}")

        # Take user input to select a subject
        print("\n")
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > len(subjects):
            print("Invalid choice. Please try again.")
            return
        selected_subject = subjects[choice - 1][0]

        # Fetch books related to the selected subject
        query = (
            f"SELECT author, title, isbn, price, subject FROM books "
            f"WHERE LOWER(subject) = LOWER('{selected_subject}')"
        )
        books = db.execute_with_fetchall(query)

        # Print the number of books available on this subject
        print(f"\n{len(books)} books available on this Subject\n")

        # Display books (2 at a time)
        for i in range(0, len(books), 2):
            for j in range(i, min(i + 2, len(books))):
                author = books[j][0] if len(books[j]) > 1 else "Unknown"
                title = books[j][1] if len(books[j]) > 2 else "Unknown"
                isbn = books[j][2] if len(books[j]) > 3 else "Unknown"
                price = books[j][3] if len(books[j]) > 4 else "Unknown"
                subject = books[j][4] if len(books[j]) > 4 else "Unknown"

                print(
                    f"Author: {author}\n Title: {title}\n "
                    f"ISBN: {isbn}\n Price: {price}\n "
                    f"Subject: {subject}\n"
                )

            # Provide options to the user
            option = input(
                "Enter ISBN to add to cart \nor \n'n' to browse \n"
                "or \npress ENTER to go back to menu: "
            )

            if option == '':
                return
            elif option.lower() == 'n':
                continue
            else:
                quantity = int(input("Enter quantity: "))
                # Add book to the cart
                db.execute_with_commit(
                    "INSERT INTO cart (userid, isbn, qty) "
                    f"VALUES ({member.userid}, '{option}', {quantity})"
                )

                if quantity:
                    print("\nBook added to the database successfully.\n")
                else:
                    print("\nFailed to add the book to the database.\n")

    # Member menu - Option 2: Search by Author/Title
    @staticmethod
    def search_by_author_title(db, member):
        while True:
            print("\n1. Author Search")
            print("2. Title Search")
            print("3. Go Back to Member Menu\n")

            option = input("Type in your option: ")

            if option == '1':
                substring = input("Enter author's name or part of it: ")
                search_type = 'author'
            elif option == '2':
                substring = input("Enter title or part of it: ")
                search_type = 'title'
            elif option == '3':
                return
            else:
                print("Invalid option, please try again")
                continue

            # Perform the search based on the user's input
            query = (
                f"SELECT author, title, isbn, price, subject "
                f"FROM books WHERE {search_type} LIKE '%{substring}%'"
            )
            books = db.execute_with_fetchall(query)

            # Display the search results
            print(f"\n{len(books)} books found\n")

            for i in range(0, len(books), 3):
                for j in range(i, min(i + 3, len(books))):
                    author = books[j][0] if len(books[j]) > 1 else "Unknown"
                    title = books[j][1] if len(books[j]) > 2 else "Unknown"
                    isbn = books[j][2] if len(books[j]) > 3 else "Unknown"
                    price = books[j][3] if len(books[j]) > 4 else "Unknown"
                    subject = books[j][4] if len(books[j]) > 4 else "Unknown"

                    print(
                        f"Author: {author}\n Title: {title}\n "
                        f"ISBN: {isbn}\n Price: {price}\n "
                        f"Subject: {subject}\n"
                    )

                # Provide options to the user
                option = input(
                    "Enter ISBN to add to cart \n"
                    "or \n'n' to browse \n"
                    "or \npress ENTER to go back to menu: "
                )

                if option == '':
                    return
                elif option.lower() == 'n':
                    continue
                else:
                    quantity = int(input("Enter quantity: "))

                    # Add book to the cart
                    db.execute_with_commit(
                        "INSERT INTO cart (userid, isbn, qty) "
                        f"VALUES ({member.userid}, '{option}', {quantity})"
                    )

                    if quantity:
                        print("\nBook added to the database successfully.\n")
                    else:
                        print("\nFailed to add the book to the database.\n")

    # Member menu - Option 3: Check Out
    @staticmethod
    def check_out(db, member):
        # Fetch cart contents
        cart_contents = db.execute_with_fetchall(f"""
            SELECT c.isbn, b.title, b.price, c.qty
            FROM cart c
            JOIN books b ON c.isbn = b.isbn
            WHERE c.userid = '{member.userid}'
        """)

        # Display cart contents header
        print("\nCurrent Cart Contents:\n")
        print("ISBN \t\t Title \t\t\t\t\t\t    $ Qty  Total")
        print("-" * 84)
        total_amount = 0

        # Display cart contents
        for cart_item in cart_contents:
            isbn, title, price, qty = cart_item
            total_item_price = price * qty

            # Display each cart item using a fixed-width format
            print(
                f"{isbn} \t {title[:40]:<45} ${price:.2f}  "
                f"{qty:<3} ${total_item_price:.2f}"
            )
            print("-" * 84)
            # Update total_amount with the current item's total price
            total_amount += total_item_price

        # Display total
        print(f"Total \t\t\t\t\t\t\t\t\t  ${total_amount:.2f}")
        print("-" * 84)
        # Ask user to proceed to check out
        proceed = input("Proceed to check out (Y/N)?: ")
        if proceed.lower() == 'y':
            # Fetch user's address
            address_details = db.execute_with_fetchall(
                f"SELECT address, city, zip "
                f"FROM members WHERE userid = '{member.userid}'"
            )

            # Check if the result is not empty
            if address_details:
                address_details = address_details[0]
            else:
                print("\nError: User address not found.")
                return  # Return or handle the error accordingly

            # Fetch the maximum ono value
            max_ono_query = "SELECT MAX(ono) FROM orders"
            max_ono_result = db.execute_with_fetchall(max_ono_query)
            max_ono = (
                max_ono_result[0][0]
                if max_ono_result and max_ono_result[0][0]
                else 0
            )

            # Increment the maximum ono to get a new unique value
            new_ono = max_ono + 1

            # Insert the order with the manually obtained ono value
            insert_order_query = (
                f"INSERT INTO orders (ono, userid, shipaddress, "
                f"shipcity, shipzip) VALUES ({new_ono}, "
                f"'{member.userid}', '{address_details[0]}', "
                f"'{address_details[1]}', '{address_details[2]}')"
            )

            # Save order to Order table
            db.execute_with_commit(insert_order_query)

            # Fetch the order id of the order just created
            max_ono_query = (
                f"SELECT MAX(ono) FROM orders "
                f"WHERE userid = '{member.userid}'"
            )
            max_ono_result = db.execute_with_fetchall(max_ono_query)
            if max_ono_result and max_ono_result[0][0] is not None:
                order_id = max_ono_result[0][0]
            else:
                print("\nError: Failed to retrieve order_id.")
                return

            # Save books to 'odetails' table
            for item in cart_contents:
                isbn, title, price, qty = item
                amount = price * qty
                odetails_query = (
                    f"INSERT INTO odetails (ono, isbn, qty, amount) "
                    f"VALUES ({order_id}, '{isbn}', {qty}, {amount})"
                )

                # Save order details to odetails table
                db.execute_with_commit(odetails_query)

                # Clear the cart after successful checkout
                db.execute_with_commit(
                    f"DELETE FROM cart "
                    f"WHERE userid = '{member.userid}'"
                )

                # Display invoice
                print(f"\n\t\t\tInvoice for Order no.{order_id}\n")
                print("Shipping Address:")
                print(f"Name: \t\t {member.fname}, {member.lname}")
                print(f"Address: \t {address_details[0]}")
                print(f"\t\t {address_details[1]}")
                print(f"\t\t {address_details[2]}")
                print("-" * 84)
                print("ISBN \t\t Title \t\t\t\t\t\t    $  Qty  Total")
                print("-" * 84)

                # Display each cart item in the invoice section
                for item in cart_contents:
                    isbn, title, price, qty = item
                    total_item_price = price * qty

                    # Display each cart item using a fixed-width format
                    print(
                        f"{isbn} \t {title[:40]:<45} ${price:.2f}  "
                        f"{qty:<3} ${total_item_price:.2f}"
                    )
                    print("-" * 84)

                # Display total and estimated delivery date
                print(f"Total = \t\t\t\t\t\t\t\t  ${total_item_price:.2f}")
                current_date = datetime.datetime.now()
                shipment_date = (
                    current_date + datetime.timedelta(days=7)
                )

                print(
                    f"\nEstimated delivery date: "
                    f"{shipment_date}\n"
                )
                input("Press enter to go back to Menu")
