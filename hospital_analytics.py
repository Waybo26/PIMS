import matplotlib.pyplot as plt
import pandas as pd

import os
from datetime import datetime

def plot_hospital_capacity(csv_filepath):
    """Plots hospital capacity by diagnosis and saves to analytics folder."""
    try:
        # Create analytics folder if it doesn't exist
        output_folder = 'analytics_reports'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"Created folder: {output_folder}")

        df = pd.read_csv(csv_filepath)
        diagnosis_counts = df['Diagnosis'].value_counts()
        
        plt.figure(figsize=(10, 6))
        diagnosis_counts.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title('Patient Counts by Diagnosis')
        plt.xlabel('Diagnosis')
        plt.ylabel('Number of Patients')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"capacity_report_{timestamp}.png"
        filepath = os.path.join(output_folder, filename)
        plt.savefig(filepath)
        plt.show()
        
        print(f"\nAnalytics report generated: {filepath}")
    except Exception as e:
        print(f"Could not plot data: {e}")
