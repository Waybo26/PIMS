from models import Patient, MedicalRecord
from data_manager import load_patient_data, get_critical_patients
from analytics import plot_hospital_capacity
from datetime import datetime

def validate_dob(dob_string: str) -> bool:
    """Validates Date of Birth format to ensure it's not in the future."""
    try:
        valid_date = datetime.strptime(dob_string, "%Y-%m-%d")
        if valid_date > datetime.now():
            raise ValueError("DOB cannot be in the future.")
        return True
    except ValueError as e:
        print(f"Invalid DOB Input: {e}")
        return False

def main():
    filepath = 'patients.csv'
    patients_list = load_patient_data(filepath)
    db_running = True

    while db_running:
        print("\n--- Hospital Database ---")
        print("1. View All Patients")
        print("2. View Critical Patients")
        print("3. Add Patient")
        print("4. Plot Hospital Capacity (Analytics)")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            for idx, p in enumerate(patients_list, start=1):
                print(f"{idx}. {p}")
        elif choice == '2':
            criticals = get_critical_patients(patients_list)
            for p in criticals:
                print(f"CRITICAL: {p}")
        elif choice == '3':
            name = input("Enter Name: ")
            dob = input("Enter DOB (YYYY-MM-DD): ")
            if validate_dob(dob):
                record = MedicalRecord("Undiagnosed", False, 0.0)
                new_p = Patient(len(patients_list) + 1, name, dob, record)
                patients_list.append(new_p)
                print("Patient added successfully!")
        elif choice == '4':
            print("Generating chart... Please close the window to continue.")
            plot_hospital_capacity(filepath)
        elif choice == '5':
            print("Shutting down system...")
            db_running = False
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
