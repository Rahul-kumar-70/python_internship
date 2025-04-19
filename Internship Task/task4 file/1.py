"""
1.create a file everytime when you are writing a notes
2.read--->exception
3.change content(permission--no write mode permission)--->exception
4.remove
5.rename
6.add content in exixting file
7.searching:string/regex
8.exit--close
"""
all_choice='''
------------------------------------------------
                1.Create File
                2.Read data
                3.Change Content
                4.remove File 
                5.Rename file
                6.Add content
                7.Search content
                8.Exit
-----------------------------------------------------
'''
print(all_choice)

import os

def create_file():
    filename=input("enter the file name:")
    try:
        with open(filename,'x') as f:
            print(f"{filename} id created")
    except FileExistsError :
        print(f" this {filename} already exit")
    except Exception as e:
        print(f'error:{e}')
def read_data():
    filename=input("enter the file name:")
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"this {filename} not found")

def change_content():
    filename=input("enter the file name:")
    try:
        with open(filename,'w') as f:
            content=input("enter the content for chnage:")
            f.write(content +'\n')
            print("content added")
    except Exception as e:
        print(f"Eroor:{f}")

def rename_file():
    old_name = input("Enter current file name: ")
    new_name = input("Enter new file name: ")
    try:
        os.rename(old_name,new_name)
        print(f'{old_name} renamed to {new_name}')
    except Exception as e:
        print(f"error:{e}")

def remove_file():
    filename=input("enter the file name:")
    try:
        os.remove(filename)
        print(f" this {filename} name removed")
    except Exception as e:
        print(f"Error:{e}")

def add_content():
    filename=input("enter the file name:")
    try:
        with open(filename,'a') as f:
            content=input("enter the content what u want to add:")
            f.write(content +'\n')
            print(f"Data Append in the {filename}")
    except Exception as e:
        print(f" Error:{e}")
def search_content():
    filename=input("enter the filename:")
    pattern=input("enter the content name u want to search:")
    try:
        with open(filename,'r') as f:
            lines=f.readlines()
            found=False
            for i,line in enumerate(lines,1):
                if pattern in line:
                    print(f"line:{i} -->{line.strip()}")
                    found=True
            if not found:
                print("Not match")
    except Exception as e:
        print(f"Error:{e}")

while True:
    choice=int(input("enter the choices:"))
    if choice==1:
        create_file()
    elif choice==2:
        read_data()
    elif choice==3:
        change_content()
    elif choice==4:
        remove_file()
    elif choice==5:
        rename_file()
    elif choice==6:
        add_content()
    elif choice==7:
        search_content()
    elif choice==8:
        print("Thanks for using this applications")
        break
    else:
        print("please enter valid choice")


