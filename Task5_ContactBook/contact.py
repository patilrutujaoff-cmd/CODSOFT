contacts = {}

print("===== CONTACT BOOK APPLICATION =====")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # ADD CONTACT
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }
        print("✅ Contact added successfully")

    # VIEW CONTACTS
    elif choice == "2":
        if not contacts:
            print("No contacts available")
        else:
            print("\n--- Contact List ---")
            for name, details in contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print("--------------------")

    # SEARCH CONTACT
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print("Contact Found:")
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
        else:
            print("❌ Contact not found")

    # UPDATE CONTACT
    elif choice == "4":
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            contacts[name]["phone"] = phone
            contacts[name]["email"] = email
            print("✅ Contact updated successfully")
        else:
            print("❌ Contact not found")

    # DELETE CONTACT
    elif choice == "5":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("✅ Contact deleted successfully")
        else:
            print("❌ Contact not found")

    # EXIT
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
