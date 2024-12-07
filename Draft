import sqlite3

# Function to display all phonebook entries
def display_phonebook():
    try:
        conn = sqlite3.connect('phonebook.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM Entries")
        rows = cursor.fetchall()

        if rows:
            print("\nPhonebook Entries:")
            for row in rows:
                print(f"Name: {row[0]}, Phone Number: {row[1]}")
        else:
            print("The phonebook is empty.")
    
    except sqlite3.Error as e:
        print("Error accessing the database:", e)
    finally:
        if conn:
            conn.close()

# Function to add a new entry
def add_entry():
    try:
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")

        conn = sqlite3.connect('phonebook.db')
        cursor = conn.cursor()

        # Check if the name already exists
        cursor.execute("SELECT * FROM Entries WHERE Name=?", (name,))
        if cursor.fetchone():
            print(f"Entry with name '{name}' already exists.")
        else:
            cursor.execute("INSERT INTO Entries (Name, PhoneNumber) VALUES (?, ?)", (name, phone_number))
            conn.commit()
            print(f"Added new entry for {name}.")
    
    except sqlite3.Error as e:
        print("Error accessing the database:", e)
    finally:
        if conn:
            conn.close()

# Function to update an existing entry
def update_entry():
    try:
        name = input("Enter the name of the person to update: ")
        new_phone_number = input("Enter the new phone number: ")

        conn = sqlite3.connect('phonebook.db')
        cursor = conn.cursor()

        # Check if the entry exists
        cursor.execute("SELECT * FROM Entries WHERE Name=?", (name,))
        if cursor.fetchone():
            cursor.execute("UPDATE Entries SET PhoneNumber=? WHERE Name=?", (new_phone_number, name))
            conn.commit()
            print(f"Updated {name}'s phone number.")
        else:
            print(f"No entry found for {name}.")
    
    except sqlite3.Error as e:
        print("Error accessing the database:", e)
    finally:
        if conn:
            conn.close()

# Function to delete an entry
def delete_entry():
    try:
        name = input("Enter the name of the person to delete: ")

        conn = sqlite3.connect('phonebook.db')
        cursor = conn.cursor()

        # Check if the entry exists
        cursor.execute("SELECT * FROM Entries WHERE Name=?", (name,))
        if cursor.fetchone():
            cursor.execute("DELETE FROM Entries WHERE Name=?", (name,))
            conn.commit()
            print(f"Deleted {name} from the phonebook.")
        else:
            print(f"No entry found for {name}.")
    
    except sqlite3.Error as e:
        print("Error accessing the database:", e)
    finally:
        if conn:
            conn.close()

# Main menu to interact with the phonebook database
def phonebook_menu():
    while True:
        print("\nPhonebook Menu:")
        print("1. Display all phonebook entries")
        print("2. Add a new entry")
        print("3. Update an existing entry")
        print("4. Delete an entry")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_phonebook()
        elif choice == '2':
            add_entry()
        elif choice == '3':
            update_entry()
        elif choice == '4':
            delete_entry()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the phonebook menu
if __name__ == "__main__":
    phonebook_menu()
