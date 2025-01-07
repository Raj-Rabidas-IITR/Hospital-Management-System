# Hospital Management System

This is a Python-based terminal application for managing hospital operations such as patient management, doctor management, appointments, and billing. The application uses MySQL as its database backend.

## Setup Instructions

Follow these steps to set up and run the application:

### 1. Clone the Repository
```bash
git clone https://github.com/Raj-Rabidas-IITR/Hospital-Management-System.git
cd Hospital-Management-System 

### 2. Install dependencies
pip install -r requirements.txt

### 3. Create a .env file
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=<your password>
DB_NAME=hospital_db

### 4. Setup your database first 
python setup_db.py


### 5. Run the main application
python main.py
