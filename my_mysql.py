import mysql.connector

def connect_to_database():
    # Establishing connection to MySQL database
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database_name"
        )
        return conn
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None

def create_table(cursor):
    # Creating table if not exists
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, email VARCHAR(255))")
    except mysql.connector.Error as e:
        print("Error creating table:", e)

def insert_data(conn, cursor, name, age, email):
    # Inserting data into the table
    try:
        cursor.execute("INSERT INTO users (name, age, email) VALUES (%s, %s, %s)", (name, age, email))
        conn.commit()
        print("Data inserted successfully!")
    except mysql.connector.Error as e:
        print("Error inserting data:", e)
        conn.rollback()

def main():
    # Taking input from user
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")

    # Connecting to database
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()

        # Creating table if not exists
        create_table(cursor)

        # Inserting data
        insert_data(conn, cursor, name, age, email)

        # Closing cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
