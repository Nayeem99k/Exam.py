# main.py

from add_contact import add_contact
from error_handling import validate_name, validate_email, validate_phone
from load_contacts import load_contacts
from prevent_duplicates import prevent_duplicates  # This should work if prevent_duplicates.py exists correctly
from remove_contact import remove_contact
from save_contacts import save_contacts
from search_contact import search_contact
from view_contacts import view_contacts

def display_menu():
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Save Contacts to File")
    print("6. Load Contacts from File")
    print("7. Prevent Duplicate Contacts")
    print("8. Error Handling (Validation)")
    print("0. Exit")

def main():
    contacts = []  # Initialize an empty list to store contacts
    load_contacts(contacts)  # Load contacts from file at the start

    while True:
        display_menu()  # Show menu options
        choice = input("Please choose an option: ")

        if choice == '1':
            add_contact(contacts)  # Call add_contact function
        elif choice == '2':
            view_contacts(contacts)  # Call view_contacts function
        elif choice == '3':
            remove_contact(contacts)  # Call remove_contact function
        elif choice == '4':
            search_contact(contacts)  # Call search_contact function
        elif choice == '5':
            save_contacts(contacts)  # Save contacts to file
        elif choice == '6':
            load_contacts(contacts)  # Load contacts from file
        elif choice == '7':
            prevent_duplicates(contacts)  # Prevent duplicate phone numbers
        elif choice == '8':
            print("Performing error handling and validation...")
            validate_name()  # Example usage of error handling
            validate_email()
            validate_phone()
        elif choice == '0':
            print("Exiting the program.")
            break  # Exit the program
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
