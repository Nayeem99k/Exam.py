def prevent_duplicates(contacts):
    phone_numbers = [contact["Phone"] for contact in contacts]
    unique_numbers = set(phone_numbers)

    if len(phone_numbers) != len(unique_numbers):
        print("Warning: There are duplicate phone numbers!")
        return False  # Duplicate found
    print("No duplicate phone numbers found.")
    return True  # No duplicates
