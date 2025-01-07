from functions import *
# from setup_db import create_database_and_tables
from color import *
# create_database_and_tables() # FIRST CONNECT TO DATABASE AND USE the database

def main_menu():
    print()
    bold_text("Welcome to Hospital Management System")
    print()

    print("1. Patient Management")
    print("2. Doctor Management")
    print("3. Appointment Management")
    print("4. Billing Management")
    print("5. Exit")
    print()
    return input("Choose an option: ")



def patient_menu():
    print()
    color_text("1. Add Patient","blue")
    color_text("2. View Patients","blue")
    color_text("3. Back to Main Menu","blue")
    return input("Choose an option: ")

def doctor_menu():
    print()
    color_text("1. Add Doctor","blue")
    color_text("2. View Doctors","blue")
    color_text("3. Back to Main Menu","blue")
    return input("Choose an option: ")

def appointment_menu():
    print()
    color_text("1. Schedule Appointment","blue")
    color_text("2. View Appointments","blue")
    color_text("3. Back to Main Menu","blue")
    return input("Choose an option: ")


def billing_menu():
    print()
    color_text("1. Create Bill","blue")
    color_text("2. View Bills","blue")
    color_text("3. Update Bill Status","blue")
    color_text("4. Back to Main Menu","blue")
    return input("Choose an option: ")



def run_billing():
    while True:
        b_choice = billing_menu()
        if b_choice == "1":
            create_bill()
        elif b_choice == "2":
            view_bills()
        elif b_choice == "3":
            update_bill_status()
        elif b_choice == "4":
            break
def run():
    while True:
        choice = main_menu()
        if choice == "1":
            while True:
                p_choice = patient_menu()
                if p_choice == "1":
                    add_patient()
                elif p_choice == "2":
                    view_patients()
                elif p_choice == "3":
                    break
        elif choice == "2":
            while True:
                d_choice = doctor_menu()
                if d_choice == "1":
                    add_doctor()
                elif d_choice == "2":
                    view_doctors()
                elif d_choice == "3":
                    break
        elif choice == "3":
            while True:
                a_choice = appointment_menu()
                if a_choice == "1":
                    add_appointment()
                elif a_choice == "2":
                    view_appointments()
                elif a_choice == "3":
                    break

        elif choice == "4":
            run_billing()
        elif choice == "4":
            color_text("Exiting the system. Goodbye!","magenta")
            break

if __name__ == "__main__":
    run()
