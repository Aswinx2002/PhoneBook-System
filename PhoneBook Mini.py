def list_contacts(phone_book):
    if not phone_book:
        print("No contacts available.")
    else:
        sorted_contacts = sorted(phone_book.items())
        print("##----Contact List----##")
        for name, number in sorted_contacts:
            print(f"{name}: {number}")


def add_contact(phone_book):
    print("##----Add Contact----##")
    while True:
        try:
            name = input("Enter the contact name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty.")
            if name in phone_book:
                raise ValueError("A contact with this name already exists.")

            number = input("Enter the phone number: ").strip()
            if len(number) != 10 or number[0] not in '6789' or not number.isdigit():
                raise ValueError("Invalid phone number. It should be a 10-digit number starting with 6, 7, 8, or 9.")

            phone_book[name] = int(number)
            print("Contact added successfully.")
            list_contacts(phone_book)
            break  # Break the loop if the contact is added successfully
        except ValueError as e:
            print(e)


def delete_contact(phone_book):
    print("##----Delete Contact----##")
    try:
        name = input("Enter the name of the contact to delete: ").strip()
        if name not in phone_book:
            raise KeyError("Contact not found.")
        del phone_book[name]
        print("Contact deleted successfully.")
        list_contacts(phone_book)
    except KeyError as e:
        print(e)


def search_contact_by_name(phone_book):
    print("##----Search Contact by Name----##")
    name = input("Enter the name to search: ").strip()
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print("Contact not found.")


def search_contact_by_number(phone_book):
    print("##----Search Contact by Number----##")
    try:
        number = input("Enter the phone number to search: ").strip()
        if not number.isdigit():
            raise ValueError("Invalid phone number format. Please enter a numeric value.")

        number = int(number)
        found = False
        for contact_name, contact_number in phone_book.items():
            if contact_number == number:
                print(f"{contact_name}: {contact_number}")
                found = True

        if not found:
            print("Contact not found.")
    except ValueError as e:
        print(e)


phone_book = {
    "Vishakh": 7968541230,
    "Aldren": 7902520048,
    "Roshan": 7999999999,
    "Anusha": 6235537565,
    "Jesly": 9645921276,
    "Tinu": 9847224787,
    "Roopak": 8426579310,
    "Aswin": 7963258410
}

while True:
    print("\nPhone Book Menu")
    print("1. List all contacts")
    print("2. Add a new contact")
    print("3. Delete a contact")
    print("4. Search contact by name")
    print("5. Search contact by number")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()
    if choice == '1':
        list_contacts(phone_book)
    elif choice == '2':
        add_contact(phone_book)
    elif choice == '3':
        delete_contact(phone_book)
    elif choice == '4':
        search_contact_by_name(phone_book)
    elif choice == '5':
        search_contact_by_number(phone_book)
    elif choice == '6':
        print("Exiting phone book.")
        break
    else:
        print("Invalid choice. Please try again.")
