from db import connect_db

def create_database_and_tables():
    try:
        # Connect to MySQL without specifying a database
        conn = connect_db()
        cursor = conn.cursor()

        # Step 1: Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS hospital_db;")
        print("Database 'hospital_db' checked/created successfully.")

        # Use the hospital_db database
        cursor.execute("USE hospital_db;")

        # Step 2: Create patients table
        patients_table = """
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            age INT NOT NULL,
            contact VARCHAR(15) NOT NULL
        );
        """
        cursor.execute(patients_table)
        print("Table 'patients' checked/created successfully.")

        # Step 3: Create doctors table
        doctors_table = """
        CREATE TABLE IF NOT EXISTS doctors (
            doctor_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            age INT NOT NULL,
            contact VARCHAR(15) NOT NULL,
            specialty VARCHAR(50) NOT NULL,
            is_available BOOLEAN DEFAULT TRUE
        );
        """
        cursor.execute(doctors_table)
        print("Table 'doctors' checked/created successfully.")

        # Step 4: Create appointments table
        appointments_table = """
        CREATE TABLE IF NOT EXISTS appointments (
            appointment_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            patient_id INT UNSIGNED NOT NULL,
            doctor_id INT UNSIGNED NOT NULL,
            date DATE NOT NULL,
            time TIME NOT NULL,
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
            FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE
        );
        """
        cursor.execute(appointments_table)
        print("Table 'appointments' checked/created successfully.")

        # Step 5: Create billing table
        billing_table = """
        CREATE TABLE IF NOT EXISTS billing (
            bill_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            patient_id INT UNSIGNED NOT NULL,
            amount FLOAT NOT NULL,
            status VARCHAR(10) DEFAULT 'Unpaid',
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
        );
        """
        cursor.execute(billing_table)
        print("Table 'billing' checked/created successfully.")

        conn.commit()  # Commit changes to the database

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Database connection closed.")

# # Call the function to create the database and tables
# if __name__ == "__main__":
#     create_database_and_tables()
