def search_contact(contacts):
    query = input("Enter Name, Email, or Phone to search: ").lower()
    results = [c for c in contacts if query in [c["Name"].lower(), c["Email"].lower(), c["Phone"]]]
    if results:
        print("\n--- Search Results ---")
        for contact in results:
            print(f"Name: {contact['Name']}, Email: {contact['Email']}, Phone: {contact['Phone']}, Address: {contact['Address']}")
    else:
        print("No matching contacts found.")