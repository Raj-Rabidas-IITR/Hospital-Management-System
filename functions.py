from prettytable import PrettyTable
from db import execute_query
from models import Patient, Doctor, Appointment, Billing
from color import *
import datetime

e = datetime.datetime.now()
todays_date = e.strftime("%Y-%m-%d")

import re

def validate_contact(contact):
    pattern = r'^\d{10}$'
    if re.match(pattern, contact):
        return True
    else:
        color_text("Invalid contact number! Must be a 10-digit number.","red")
        return False
    

def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    contact = input("Enter patient contact: ")

    while not validate_contact(contact):

        contact = input("Enter patient contact: ")

    query = "INSERT INTO patients (name, age, contact) VALUES (%s, %s, %s)"
    execute_query(query, (name, age, contact))

    query = "SELECT LAST_INSERT_ID() AS patient_id"
    patient = execute_query(query, fetch=True)
    color_text(f"Patient added successfully! Assigned Patient ID: {patient[0]['patient_id']}","green")



def view_patients():
    query = "SELECT * FROM patients"
    patients = execute_query(query, fetch=True)
    table = PrettyTable(["Patient ID", "Name", "Age", "Contact"])
    for patient in patients:
        table.add_row([patient["patient_id"], patient["name"], patient["age"], patient["contact"]])
    print(table)



def add_appointment():
    view_patients()
    
    patient_id = input("Enter patient ID: ")
    view_doctors()

    doctor_id = input("Enter doctor ID: ")
    
    query = "SELECT is_available FROM doctors WHERE doctor_id = %s"
    doctor = execute_query(query, (doctor_id,), fetch=True)
    if not doctor or not doctor[0]['is_available']:
        color_text("Doctor is not available for appointments!","yellow")
        return

    date = input("Enter appointment date (YYYY-MM-DD)/today?: ")
    
    while True:
        time = input("Enter appointment time (HH:MM): ")
        # Validate the time format using regex
        if re.match(r"^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$", time):
            # print("Valid time entered:", time)
            break
        else:
            color_text("Invalid time format. Please enter the time in HH:MM format (24-hour clock).","yellow")



    if(date==""):
        date=todays_date

    

    try:
        query = "INSERT INTO appointments (patient_id, doctor_id, date, time) VALUES (%s, %s, %s, %s)"
        execute_query(query, (patient_id, doctor_id, date, time))

        query = "SELECT LAST_INSERT_ID() AS appointment_id"
        appointment = execute_query(query, fetch=True)
        color_text(f"Appointment scheduled successfully! Assigned Appointment ID: {appointment[0]['appointment_id']}","green")
    except:
        color_text("Invalid patient ID!! ","red")




def add_doctor():
    name = input("Enter doctor name: ")
    age = int(input("Enter doctor age: "))
    contact = input("Enter doctor contact: ")

    while not validate_contact(contact):
        contact = input("Enter doctor contact: ")

    specialty = input("Enter specialty: ")

    query = "INSERT INTO doctors (name, age, contact, specialty) VALUES (%s, %s, %s, %s)"
    execute_query(query, (name, age, contact, specialty))

    query = "SELECT LAST_INSERT_ID() AS doctor_id"
    doctor = execute_query(query, fetch=True)
    color_text(f"Doctor added successfully! Assigned Doctor ID: {doctor[0]['doctor_id']}","green")



def view_doctors():
    query = "SELECT * FROM doctors"
    doctors = execute_query(query, fetch=True)
    table = PrettyTable(["Doctor ID", "Name", "Age", "Contact", "Specialty"])
    for doctor in doctors:
        table.add_row([doctor["doctor_id"], doctor["name"], doctor["age"], doctor["contact"], doctor["specialty"]])
    print(table)



def view_appointments():
    query = """
    SELECT 
        appointments.appointment_id,
        patients.name AS patient_name,
        doctors.name AS doctor_name,
        appointments.date,
        appointments.time
    FROM 
        appointments
    INNER JOIN 
        patients ON appointments.patient_id = patients.patient_id
    INNER JOIN 
        doctors ON appointments.doctor_id = doctors.doctor_id;
    """
    appointments = execute_query(query, fetch=True)
    
    # Create a PrettyTable to display the data
    table = PrettyTable(["Appointment ID", "Patient Name", "Doctor Name", "Date", "Time"])
    for appointment in appointments:
        table.add_row([
            appointment["appointment_id"],
            appointment["patient_name"],
            appointment["doctor_name"],
            appointment["date"],
            appointment["time"]
        ])
    print(table)
    
def create_bill():
    view_patients()
    patient_id = input("Enter patient ID: ")
    amount = float(input("Enter bill amount: "))
    try:

        query = "INSERT INTO billing (patient_id, amount) VALUES (%s, %s)"
        execute_query(query, (patient_id, amount))

        query = "SELECT LAST_INSERT_ID() AS bill_id"
        bill = execute_query(query, fetch=True)
        color_text(f"Bill created successfully! Assigned Bill ID: {bill[0]['bill_id']}","green")
    except:
        color_text("Invalid Patient ID!!","red")

def view_bills():
    query = "SELECT * FROM billing"
    bills = execute_query(query, fetch=True)
    table = PrettyTable(["Bill ID", "Patient ID", "Amount", "Status"])
    for bill in bills:
        table.add_row([bill["bill_id"], bill["patient_id"], bill["amount"], bill["status"]])
    print(table)

def update_bill_status():
    bill_id = input("Enter bill ID: ")
    new_status = input("Enter new status (Paid/Unpaid): ")
    try:
    
        query = "UPDATE billing SET status = %s WHERE bill_id = %s"
        execute_query(query, (new_status, bill_id))
        color_text("Bill status updated successfully!","green")
    except:
        color_text("Invalid Bill Id!","red")
