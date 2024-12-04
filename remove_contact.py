from save_contacts import FILE_NAME
import csv

def remove_contact(contacts):
    try:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['Name']} ({contact['Phone']})")
        index = int(input("Enter the number of the contact to remove: ")) - 1

        if 0 <= index < len(contacts):
            removed_contact = contacts.pop(index)
            print(f"Contact {removed_contact['Name']} removed successfully!")

            # Overwrite file
            with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=["Name", "Email", "Phone", "Address"])
                writer.writeheader()
                writer.writerows(contacts)
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
