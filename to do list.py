# Import necessary modules
import os

# Create a dictionary to store contact details
contacts = {}

# Function to add a new contact
def add_contact():
  name = input("Enter the contact name: ")
  phone_number = input("Enter the contact phone number: ")
  email = input("Enter the contact email address: ")
  address = input("Enter the contact address: ")

  contacts[name] = {
    "phone_number": phone_number,
    "email": email,
    "address": address
  }

  print("Contact {} added successfully!".format(name))

# Function to view the contact list
def view_contact_list():
  if len(contacts) == 0:
    print("There are no contacts in the contact book.")
  else:
    for name, details in contacts.items():
      print("Name:", name)
      print("Phone number:", details["phone_number"])
      print("Email address:", details["email"])
      print("Address:", details["address"])

# Function to search for a contact
def search_contact():
  name = input("Enter the contact name or phone number: ")

  if name in contacts:
    details = contacts[name]
    print("Contact details:")
    print("Name:", name)
    print("Phone number:", details["phone_number"])
    print("Email address:", details["email"])
    print("Address:", details["address"])
  else:
    print("Contact not found.")

# Function to update a contact
def update_contact():
  name = input("Enter the contact name: ")

  if name in contacts:
    details = contacts[name]

    phone_number = input("Enter the new phone number (leave blank if no change): ")
    if phone_number:
      details["phone_number"] = phone_number

    email = input("Enter the new email address (leave blank if no change): ")
    if email:
      details["email"] = email

    address = input("Enter the new address (leave blank if no change): ")
    if address:
      details["address"] = address

    print("Contact details updated successfully!")
  else:
    print("Contact not found.")

# Function to delete a contact
def delete_contact():
  name = input("Enter the contact name to delete: ")

  if name in contacts:
    del contacts[name]
    print("Contact deleted successfully!")
  else:
    print("Contact not found.")

# Main function
def main():
  while True:
    print("Welcome to the Contact Book!")
    print("1. Add contact")
    print("2. View contact list")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      add_contact()
    elif choice == "2":
      view_contact_list()
    elif choice == "3":
      search_contact()
    elif choice == "4":
      update_contact()
    elif choice == "5":
      delete_contact()
    elif choice == "6":
      break
    else:
      print("Invalid choice.")

# Start the program
if __name__ == "__main__":
  main()
