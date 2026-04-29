import matplotlib.pyplot as plt
import pandas as pd

def plot_hospital_capacity(csv_filepath):
    """Plots hospital capacity by diagnosis using Matplotlib."""
    try:
        df = pd.read_csv(csv_filepath)
        diagnosis_counts = df['Diagnosis'].value_counts()
        
        diagnosis_counts.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title('Patient Counts by Diagnosis')
        plt.xlabel('Diagnosis')
        plt.ylabel('Number of Patients')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Could not plot data: {e}")
