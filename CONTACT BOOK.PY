#==============================
# I am creating a Contact Book.
#==============================



contacts = []  # List to store contact dictionaries

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("✅ Contact added successfully!")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\n--- Search Contact ---")
    keyword = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if keyword.lower() in contact["name"].lower() or keyword in contact["phone"]:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("❌ Contact not found.")

def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Leave field empty to keep current value.")
            new_phone = input(f"Enter new phone ({contact['phone']}): ") or contact["phone"]
            new_email = input(f"Enter new email ({contact['email']}): ") or contact["email"]
            new_address = input(f"Enter new address ({contact['address']}): ") or contact["address"]

            contact["phone"] = new_phone
            contact["email"] = new_email
            contact["address"] = new_address
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("✅ Contact deleted successfully!")
            return
    print("❌ Contact not found.")

# Main Menu
while True:
    print("\n📒 Contact Book Menu")
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
        print("👋 Exiting Contact Book. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please select 1-6.")

