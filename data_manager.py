import pandas as pd
from models import Patient, MedicalRecord
from datetime import datetime

# validation functions
def validate_dob(dob_string):
    '''
    Validates Date of Birth format to ensure it's not in the future.
    '''
    try:
        valid_date = datetime.strptime(dob_string, "%Y-%m-%d")
        if valid_date > datetime.now():
            raise ValueError("DOB cannot be in the future.")
        return True
    except ValueError as e:
        print(f"Invalid DOB Input: {e}")
        return False

def validate_name(name):
    '''
    Validates name to ensure it's not empty and contains only letters and spaces.
    '''
    if not name.strip():
        print("Invalid Name Input: Name cannot be empty.")
        return False
    if not all(x.isalpha() or x.isspace() for x in name):
        print("Invalid Name Input: Name must contain only letters and spaces.")
        return False
    return True

# data loading/saving 
def load_patient_data(filepath):
    """Loads raw patient data using Pandas."""
    try:
        df = pd.read_csv(filepath)
        patients = []
        for _, row in df.iterrows():
            record = MedicalRecord(row['Diagnosis'], bool(row['IsCritical']), float(row['Balance']))
            if pd.notna(row['Prescription']):
                record.prescriptions.add(row['Prescription'])
            if pd.notna(row['Allergy']):
                record.allergies.add(row['Allergy'])
            
            patient = Patient(int(row['PatientID']), row['Name'], row['DOB'], record)
            patients.append(patient)
        return patients
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def get_critical_patients(patients):
    """List comprehension to filter critical patients."""
    return [p for p in patients if p.is_critical]

def save_patient_data(filepath: str, patients: list):
    """Saves patient list back to CSV."""
    try:
        data = []
        for p in patients:
            data.append({
                'PatientID': p.patient_id,
                'Name': p.name,
                'DOB': p.dob,
                'Diagnosis': p.record.diagnosis,
                'IsCritical': p.record.is_critical,
                'Balance': p.record.balance,
                'Prescription': ', '.join(p.record.prescriptions) if p.record.prescriptions else None,
                'Allergy': ', '.join(p.record.allergies) if p.record.allergies else None
            })
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)
    except Exception as e:
        print(f"Error saving data: {e}")

def update_patient(patients: list, patient_id: int, new_name: str, new_dob: str, new_diagnosis: str, is_critical: bool) -> bool:
    """Updates an existing patient's details."""
    for p in patients:
        if p.patient_id == patient_id:
            p.name = new_name
            p.dob = new_dob
            p.record.diagnosis = new_diagnosis
            p.record.is_critical = is_critical
            return True
    return False

def delete_patient(patients: list, patient_id: int) -> bool:
    """Deletes a patient from the list by ID."""
    for i, p in enumerate(patients):
        if p.patient_id == patient_id:
            patients.pop(i)
            return True
    return False

def recent_patient_generator(patients: list):
    """Generator yielding patients in reverse (most recent first)."""
    for patient in reversed(patients):
        yield patient
