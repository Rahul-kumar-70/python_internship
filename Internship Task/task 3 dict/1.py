import json

DB_FILE = "dict_db.json"
def load_db():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

def create_entry(key, value):
    if key in db:
        print(f"'{key}' already exists.")
    else:
        db[key] = value
        save_db(db)
        print(f"'{key}' added.")

def read_entry(key):
    if key in db:
        print(f"{key} → {db[key]}")
    else:
        print(f"'{key}' not found.")

def update_entry(key, new_value):
    if key in db:
        db[key] = new_value
        save_db(db)
        print(f"{key} updated.")
    else:
        print(f"'{key}' not found.")

def delete_entry(key):
    if key in db:
        del db[key]
        save_db(db)
        print(f"'{key}' deleted.")
    else:
        print(f"'{key}' not found.")

db = load_db()

while True:
    print("\n--- Simple Dict DB ---")
    print("1. Create Entry")
    print("2. Read Entry")
    print("3. Update Entry")
    print("4. Delete Entry")
    print("5. View All")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        k = input("Enter key: ")
        v = input("Enter value: ")
        create_entry(k, v)

    elif choice == "2":
        k = input("Enter key to read: ")
        read_entry(k)

    elif choice == "3":
        k = input("Enter key to update: ")
        nv = input("Enter new value: ")
        update_entry(k, nv)

    elif choice == "4":
        k = input("Enter key to delete: ")
        delete_entry(k)

    elif choice == "5":
        print("\nFull Data:", db)

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
