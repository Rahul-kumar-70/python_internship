"""
Task 1: Build a Simple Contact Book
Problem Statement:Create a command-line contact book application that
allows users to add, search, and delete contacts.
Steps to Complete:
1. Use a dictionary to store contact names and phone numbers.
2. Implement functions to add, search, and delete contacts.
3. Ensure the application handles user input correctly.
Tools/Datasets/Platforms:
Programming Language: Python 3.x.
"""

option="""
        -------------------------------
           1.Add contact
           2.Search contact
           3.delete contact
           4.Exit
        ------------------------------
"""
print(option)
dictionary={}
def add_contact():
    try:
        name=input("enter the name:")
        phone=input("enter the phone number:")
        if name not in dictionary:
            dictionary[name]=phone
        else:
            print("this name is already here so please text another name")
    except Exception as e:
        print(e)

def search_contact():
    try:
        name=input("enter the name:")
        if name in dictionary:
            print(name,'=',dictionary[name])
        else:
            print("not any contact for this name")
    except Exception as e:
        print(e)
def delete_contact():
    try:
        name=input("enter the name:")
        if name in dictionary:
            del dictionary[name]
            print("this contact is deleted")
    except Exception as e:
        print(e)
while True:
    try:
        choice = int(input("enter the choice:"))
        if choice == 1:
            add_contact()
        elif choice == 2:
            search_contact()
        elif choice == 3:
            delete_contact()
        elif choice == 4:
            break
        else:
            print("invalid choice please choice valid choice ")
    except Exception as e:
        print(e)