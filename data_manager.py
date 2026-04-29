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

def save_patient_data(filepath: str, patients: list):
    """Saves patient list back to CSV."""
    try:
        data = []
        for p in patients:
            data.append({
                'PatientID': p.patient_id,
                'Name': p.name,
                'DOB': p.dob,
                'Diagnosis': p.medical_record.diagnosis,
                'IsCritical': p.medical_record.is_critical,
                'Balance': p.medical_record.balance,
                'Prescription': ', '.join(p.medical_record.prescriptions) if p.medical_record.prescriptions else None,
                'Allergy': ', '.join(p.medical_record.allergies) if p.medical_record.allergies else None
            })
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)
    except Exception as e:
        print(f"Error saving data: {e}")

def recent_patient_generator(patients: list):
    """Generator yielding patients in reverse (most recent first)."""
    for patient in reversed(patients):
        yield patient
