import sqlite3

def display_cities():
    try:
        # Connect to the cities.db database
        conn = sqlite3.connect('cities.db')
        cursor = conn.cursor()

        while True:
            print("\nSelect an operation:")
            print("1. Display cities sorted by population (ascending)")
            print("2. Display cities sorted by population (descending)")
            print("3. Display cities sorted by name")
            print("4. Display total population")
            print("5. Display average population")
            print("6. Display city with the highest population")
            print("7. Display city with the lowest population")
            print("8. Exit")

            choice = input("Enter your choice (1-8): ")

            # Handle each choice
            if choice == '1':  # Ascending population
                cursor.execute("SELECT * FROM Cities ORDER BY Population ASC")
                results = cursor.fetchall()
                print("\nCities sorted by population (ascending):")
            elif choice == '2':  # Descending population
                cursor.execute("SELECT * FROM Cities ORDER BY Population DESC")
                results = cursor.fetchall()
                print("\nCities sorted by population (descending):")
            elif choice == '3':  # Sorted by name
                cursor.execute("SELECT * FROM Cities ORDER BY CityName ASC")
                results = cursor.fetchall()
                print("\nCities sorted by name:")
            elif choice == '4':  # Total population
                cursor.execute("SELECT SUM(Population) FROM Cities")
                total_population = cursor.fetchone()[0]
                print(f"\nTotal population: {total_population}")
                continue
            elif choice == '5':  # Average population
                cursor.execute("SELECT AVG(Population) FROM Cities")
                average_population = cursor.fetchone()[0]
                print(f"\nAverage population: {average_population}")
                continue
            elif choice == '6':  # City with the highest population
                cursor.execute("SELECT * FROM Cities ORDER BY Population DESC LIMIT 1")
                result = cursor.fetchone()
                print(f"\nCity with the highest population: {result[1]} ({result[2]})")
                continue
            elif choice == '7':  # City with the lowest population
                cursor.execute("SELECT * FROM Cities ORDER BY Population ASC LIMIT 1")
                result = cursor.fetchone()
                print(f"\nCity with the lowest population: {result[1]} ({result[2]})")
                continue
            elif choice == '8':  # Exit
                print("Exiting the program.")
                break
            else:
                print("Invalid choice, please try again.")
                continue

            # Display results for queries that return multiple rows
            for row in results:
                print(f"CityID: {row[0]}, CityName: {row[1]}, Population: {row[2]}")

    except sqlite3.Error as e:
        print("Error accessing the database:", e)
    finally:
        if conn:
            conn.close()  # Ensure the connection is closed

# Call the function to run the program
display_cities()
