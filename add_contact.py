from error_handling import validate_name, validate_email, validate_phone

def add_contact(contacts):
    try:
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")
        address = input("Enter Address: ")

        # Validate inputs
        validate_name(name)
        validate_email(email)
        validate_phone(phone)

        # Create new contact
        new_contact = {"Name": name, "Email": email, "Phone": phone, "Address": address}
        contacts.append(new_contact)
        print("Contact added successfully!")
        return new_contact
    except ValueError as e:
        print(f"Error: {e}")
        return None