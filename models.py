class MedicalRecord:
    """Represents a patient's medical history, treatments, and billing."""
    def __init__(self, diagnosis: str, is_critical: bool, balance: float):
        self.diagnosis = diagnosis
        self.is_critical = is_critical
        self.balance = balance
        self.prescriptions = set()
        self.allergies = set()
        
    def add_prescription(self, medication: str):
        if medication in self.allergies:
            return f"WARNING: Allergic to {medication}!"
        self.prescriptions.add(medication)
        return f"Added {medication}"

    def __add__(self, other):
        """Operator overload to sum balances."""
        return self.balance + other.balance

class Patient:
    """Represents a Patient using composition (has a MedicalRecord)."""
    def __init__(self, patient_id: int, name: str, dob: str, record: MedicalRecord):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.record = record
        
    def __str__(self):
        return f"Patient {self.patient_id}: {self.name} (DOB: {self.dob}) - Diagnosis: {self.diagnosis}"

    def __eq__(self, other):
        """Checks equality based on Patient ID."""
        return self.patient_id == other.patient_id

    def __getattr__(self, attr):
        """Delegates unknown attributes to the MedicalRecord."""
        return getattr(self.record, attr)
