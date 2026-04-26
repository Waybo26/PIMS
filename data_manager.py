import pandas as pd
from models import Patient, MedicalRecord

def load_patient_data(filepath: str) -> list:
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

def get_critical_patients(patients: list) -> list:
    """List comprehension to filter critical patients."""
    return [p for p in patients if p.is_critical]

def recent_patient_generator(patients: list):
    """Generator yielding patients in reverse (most recent first)."""
    for patient in reversed(patients):
        yield patient
