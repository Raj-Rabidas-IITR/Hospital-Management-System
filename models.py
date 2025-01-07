class Person:
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact


class Patient(Person):
    def __init__(self, patient_id, name, age, contact):
        super().__init__(name, age, contact)
        self.patient_id = patient_id


class Doctor(Person):
    def __init__(self, doctor_id, name, age, contact, specialty):
        super().__init__(name, age, contact)
        self.doctor_id = doctor_id
        self.specialty = specialty


class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time


class Billing:
    def __init__(self, bill_id, patient_id, amount, status="Unpaid"):
        self.bill_id = bill_id
        self.patient_id = patient_id
        self.amount = amount
        self.status = status
