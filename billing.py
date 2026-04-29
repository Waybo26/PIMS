'''
Handles billing, insurance simulation, and safety checks
'''
import random 

def flatten_charges(charges):
    '''
    This function is used to flatten nested charge lists into a single list by using recursion
    '''
    flat = []
    for item in charges:
        if type(item) == list:
            flat = flat + flatten_charges(item) #recursion is used to concatenate nested lists
        else:
            flat = flat + [item]
    return flat


def check_allergy_conflicts(record):
    '''
    This function uses set intersection to check if prescription conflict with allergies
    '''
############ double check ##############
    return record.prescriptions.intersection(record.allergies)


def generate_invoice(patient):
    '''
    This function generates an invoice for a patient which includes insurance coverage (randomized), recursive charge handling, and allergy conflict warnings
    '''

    charges = [patient.record.balance, [50, 100], 25]

    flat_charges = flatten_charges(charges)
    total_cost = sum(flat_charges)

############ double check ##############
    insurance_coverage = random.uniform(0.5, 0.9) # 50%-90%
    covered_amt = total_cost * insurance_coverage
    amt_due  = total_cost - covered_amt
    conflicts = check_allergy_conflicts(patient.record)

############ double check ##############
    invoice = f"""Invoice:
    Patient: {patient.name}
    Total Cost: ${total_cost:.2f}
    Insurance Covered: ${covered_amt:.2f}
    Amount Due: ${amt_due:.2f}
    """

    if conflicts:
        invoice += f"\n WARNING: Allergy conflict with {list(conflicts)}"
    return invoice