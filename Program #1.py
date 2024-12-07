import sqlite3

def create_cities_db():
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()
    
    # Create the Cities table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Cities (
                        CityID INTEGER PRIMARY KEY,
                        CityName TEXT,
                        Population REAL
                    )''')

    # Insert sample data
    cities_data = [
        ("New York", 8419000),
        ("Los Angeles", 3980000),
        ("Chicago", 2716000),
        ("Houston", 2328000),
        ("Phoenix", 1690000),
        ("Philadelphia", 1584000),
        ("San Antonio", 1548000),
        ("San Diego", 1424000),
        ("Dallas", 1341000),
        ("San Jose", 1027000),
        # Add more cities to total 20 rows...
    ]
    
    # Populate the table
    cursor.executemany('INSERT INTO Cities (CityName, Population) VALUES (?, ?)', cities_data)
    
    conn.commit()
    conn.close()

create_cities_db()
print("Cities database created and populated.")
