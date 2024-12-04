# load_contacts.py

def load_contacts(contacts):
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                contact = line.strip().split(",")
                name, email, phone, address = contact[0], contact[1], contact[2], contact[3]
                contacts.append({"Name": name, "Email": email, "Phone": phone, "Address": address})
    except FileNotFoundError:
        print("No previous contact data found. Starting with an empty contact book.")
