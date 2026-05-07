# Patient Information Management System

## Team
- Wesley Nabo; wnabo@stevens.edu; 20006306
- Bao-Chau Nguyen; bnguyen5@stevens.edu; 20006303

## Description

### Project Overview

Hospitals must manage large amounts of patient information, including medical history, treatment plans, and insurance data, which can become difficult to organize and analyze efficiently. A centralized patient information management system can help streamline record keeping, improve administrative decision-making, and allow healthcare staff to quickly access accurate patient data when providing care. 

Our team aims to create a patient information management system that will support hospitals. Our goal is for our project to aid in tasks like administrative reporting, creating patient profiles from analyzing raw patient data, and managing billing and financial operations. Users will be able to utilize the above three functionalities in one sitting, allowing for quick and efficient data access.

### Dependencies/Libraries
These must be installed on your laptop for this project to be successfully run

- Python 3.12+
- pandas - used to load and parse patient data from patients.csv
- matplotlib - used to generate bar charts of patient counts by diagnosis
- pytest - used to run the test suite in test_system.py
- random (built in) - used in billing.py to simulate insurance coverage percentages


### File/Module Structure

Project
|
|--- main.ipynb                 # Main program entry point in Jupyter Notebook
|--- patients.csv               # Dataset with sample patient data
|
|--- models.py                  # Contains Patient and MedicalRecord classes
|--- data_manager.py            # Functions for loading CSV data and filtering
|--- hospital_analytics.py      # Plotting function for hospital capacity chart
|--- billing.py                 # Invoice generation, charge flattening, allergy conflict checking
|
|--- test_system.py             # Pytest cases for DOB validation, patient equality, and billing



## How to run the program:

### Required Modules/Versions
- Python 3.8+
- pandas
- matplotlib
- pytest

### Execution Instructions
Run the main script:
`python main.ipynb`

Run the tests:
`pytest test_system.py`

#i# Main contributions of each team member

This project was originally created with the intention of being completed by a three member team, however, one of the team members had to leave the class. Therefore, the work for this project was distributed as follows:

Wes:
- started main notebook file, main.ipnyb
- created models.py 
- created test_system.py
- 


Bao-Chau:
- created hospital_analytics.py
- created data_manager.py
- created patients.csv
- created billing.py 

Documentation & Presentation (15 points)
README file with setup instructions (5 points). Users should be able to run the project easily by following the provided README file.
Explanation of problem and solution approach (5 points). The submission should explain what problem is being solved and how the program addresses it.
Proper file submission (all needed files included and organized) (5 points). All files must be complete, well-named, and organized so the graders can run and review the project without difficulty.