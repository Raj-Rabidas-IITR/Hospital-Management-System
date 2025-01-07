# **Hospital Management System**

This is a Python-based terminal application for managing hospital operations such as patient management, doctor management, appointments, and billing. The application uses MySQL as its database backend.

## **Setup Instructions**

Follow these steps to set up and run the application:

### **1. Clone the Repository**
```bash
git clone https://github.com/Raj-Rabidas-IITR/Hospital-Management-System.git
cd Hospital-Management-System
2. Install Dependencies
Ensure you have Python installed. Use the following command to install the required dependencies:

bash
Copy code
pip install -r requirements.txt
3. Create a .env File
Create a .env file in the root directory of the project and specify your MySQL credentials:

env
Copy code
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=<your password>
DB_NAME=hospital_db
4. Set Up the Database
Run the setup_db.py script to create the required database and tables:

bash
Copy code
python setup_db.py
5. Run the Application
Start the main application:

bash
Copy code
python main.py
Features
Patient Management: Add and view patient records.
Doctor Management: Add and view doctor records.
Appointment Management: Schedule and view appointments.
Billing System: Generate and manage patient bills.
Project Structure
bash
Copy code
Hospital-Management-System/
│
├── models.py          # Contains object-oriented models for the application
├── functions.py       # Business logic and database interaction
├── setup_db.py        # Script to set up the database and tables
├── main.py            # Entry point for the application
├── requirements.txt   # List of Python dependencies
├── .env               # Environment file for database configuration
└── README.md          # Project documentation
Additional Notes
Ensure that MySQL is installed and running on your system.
If you encounter any issues with MySQL connection, double-check your .env file and ensure the database credentials are correct.
For any errors, check the terminal output for debugging information.
