contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("Contact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    results = {name: details for name, details in contacts.items() if search_term in name or search_term in details['phone']}
    if not results:
        print("No matching contacts found.")
        return

    print("Search Results:")
    for name, details in results.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter new phone number (leave blank to skip): ")
    email = input("Enter new email (leave blank to skip): ")
    address = input("Enter new address (leave blank to skip): ")

    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address

    print(f"Contact {name} updated successfully!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
