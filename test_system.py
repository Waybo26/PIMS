import pytest
from main import validate_dob
from models import Patient, MedicalRecord
from billing import generate_invoice

def test_validate_dob_valid():
    assert validate_dob("1990-01-01") == True

def test_validate_dob_invalid_future():
    # Future dates should return False
    assert validate_dob("2050-01-01") == False

def test_validate_dob_invalid_format():
    # Wrong format should return False
    assert validate_dob("01-01-1990") == False
    
def test_patient_equality():
    r1 = MedicalRecord("Flu", False, 100)
    p1 = Patient(1, "John", "1990-01-01", r1)
    p2 = Patient(1, "Jane", "1992-02-02", r1) 
    assert p1 == p2  # True because patient_id is the same (1)

def test_generate_invoice():
    record = MedicalRecord("Flu", False, 100.0)
    record.prescriptions.add("DrugA")
    record.allergies.add("DrugA") # conflict

    patient = Patient(1, "Test Patient", "2000-01-01", record)

    invoice, amt_due = generate_invoice(patient)

    assert "Invoice" in invoice
    assert "WARNING" in invoice # so that set intersection worked
    assert amt_due > 0

