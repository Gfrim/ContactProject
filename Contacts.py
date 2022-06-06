from os import system
import time
from Contact_Console_App import Contact

contact = Contact()
def header():
    system('cls')
    for i in range(100):
        print('*', end='')
    for i in range(60):
        print(' ', end='')
    print("Contacts App")
    for i in range(100):
        print('*', end='')

def head():
    system('cls')
    for i in range(100):
        print('*', end='')
    for i in range(60):
        print(' ', end='')
    print("Contacts")
    for i in range(100):
        print('*', end='')

def add_contact():
    persons = int(input("\nEnter the number of persons to add to the contact: "))
    for i in range(persons):
        person = str(input("\nEnter the name of the new contact: "))
        number = str(input("Enter the phone number: "))
        contact.add_Contact(person,number)

def delete_contact():
    name = str(input("\nEnter the name of contact you would want to delete: "))
    contact.delete_Contact(name)

def search_contact():
    name = str(input("\nEnter the name to be searched: "))
    contact.search_Contact(name)
    if contact.search_Contact(name):
        print('Name Found!')
    else:
        print('Name not Found!')

def update_contact():
    choice = str(input("\nDo you want to update a name[Y/N]: "))
    if choice in ['Y','y']:
        name = str(input("\nEnter name you want to change: "))
        #if contact.search_Contact(name):
        new_name = str(input("Enter new name: "))
        contact.update_Contact(name, new_name)
        print('\nName changed successfully!')
        #else:
         #   print('\nName not found!')
#print('\n')
    elif choice in ['N','n']:
        print('\nOkay, your choice is my command!')
    else:
        print("Wrong Choice!")

def sort_contact():
    contact.sort_Contacts()

def show_contacts():
    contact.show_Contacts()


start = 'y'
while start in ['y','Y']:
    choices  = {1:'add', 2:'delete', 3:'search', 4:'update', 5:'sort', 6:'show'}
    header()
    for i in choices:
        print(f'\n{i}      =>      {choices[i]}')
    choose = int(input("\nChoose an operation from the options above: "))
    if choose == 1:
        head()
        add_contact()
        time.sleep(2)
    elif choose == 2:
        head()
        delete_contact()
        time.sleep(2)
    elif choose == 3:
        head()
        search_contact()
        time.sleep(2)
    elif choose == 4:
        head()
        update_contact()
        time.sleep(2)
    elif choose == 5:
        head()
        sort_contact()
        time.sleep(2)
    elif choose == 6:
        head()
        show_contacts()
        time.sleep(2)
    else:
        head()
        print("\nSorry, wrong choice made!!")
        time.sleep(1)
    start = str(input("\nDo you want to continue [Y/N]: "))
else:
    head()
    print("\nThank you!!!")
