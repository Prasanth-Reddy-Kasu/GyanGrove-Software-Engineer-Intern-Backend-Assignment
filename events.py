import sqlite3
import csv

def create_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('events.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Define the SQL query to create the events table if it does not exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY,
        event_name TEXT,
        city_name TEXT,
        date TEXT,
        time TEXT,
        latitude REAL,
        longitude REAL
    );
    """
    # Execute the create table query
    cursor.execute(create_table_query)
    # Commit the transaction
    conn.commit()
    # Close the cursor
    cursor.close()
    # Close the database connection
    conn.close()

def clear_existing_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('events.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Define the SQL query to delete all data from the events table
    clear_data_query = "DELETE FROM events;"
    # Execute the delete query
    cursor.execute(clear_data_query)
    # Commit the transaction
    conn.commit()
    # Close the cursor
    cursor.close()
    # Close the database connection
    conn.close()

def insert_data_from_csv():
    # Connect to the SQLite database
    conn = sqlite3.connect('events.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Define the file path of the CSV file containing the data
    csv_file_path = r"C:\Users\Luffy\Desktop\GyanGrove Backend Assignment\Backend_assignment_gg_dataset - dataset.csv"
    # Open the CSV file in read mode
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        # Create a CSV reader object
        csv_reader = csv.reader(csvfile)
        # Skip the header row
        next(csv_reader)
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Define the SQL query to insert data into the events table
            insert_query = """
            INSERT INTO events (event_name, city_name, date, time, latitude, longitude)
            VALUES (?, ?, ?, ?, ?, ?);
            """
            # Execute the insert query with the current row of data
            cursor.execute(insert_query, row)
    # Commit the transaction
    conn.commit()
    # Close the cursor
    cursor.close()
    # Close the database connection
    conn.close()

def main():
    # Create the events table in the database
    create_database()
    # Clear any existing data in the events table
    clear_existing_data()
    print("Data cleared successfully.")
    # Insert data from the CSV file into the events table
    insert_data_from_csv()
    print("Data added successfully.")

if __name__ == "__main__":
    main()
