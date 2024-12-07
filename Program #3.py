import sqlite3

def create_phonebook():
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()

    # Create the Entries table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Entries (
                        Name TEXT PRIMARY KEY,
                        PhoneNumber TEXT
                    )''')

    conn.commit()
    conn.close()

create_phonebook()
print("Phonebook database created.")
