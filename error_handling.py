def validate_name(name):
    if not isinstance(name, str) or not name.isalpha():
        raise ValueError("The contact’s name must be a valid string (only alphabets).")
    return True

def validate_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("The email address must be in the correct format.")
    return True

def validate_phone(phone):
    if not phone.isdigit():
        raise ValueError("The phone number must be an integer.")
    return True
