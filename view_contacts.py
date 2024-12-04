def view_contacts(contacts):
    if contacts:
        print("\n--- All Contacts ---")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['Name']}, Email: {contact['Email']}, Phone: {contact['Phone']}, Address: {contact['Address']}")
    else:
        print("No contacts found.")
