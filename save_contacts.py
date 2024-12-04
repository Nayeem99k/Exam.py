import csv

FILE_NAME = "contacts.csv"

def save_contacts(contact):
    with open(FILE_NAME, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Email", "Phone", "Address"])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(contact)
