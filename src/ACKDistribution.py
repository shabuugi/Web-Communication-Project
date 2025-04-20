import pandas as pd
import matplotlib.pyplot as plt

# List of CSV file paths
file_paths = [
    'zoom.csv',
    'youtube.csv',
    'spotify.csv',
    'google.csv',
    'edge.csv'
]
file_labels = ['Zoom', 'YouTube', 'Spotify', 'Google', 'Edge']

for label, file_path in zip(file_labels, file_paths):
    df = pd.read_csv(file_path)
    # keeping only the rows that are TCP and that has a value in the flags column
    df = df[(df['Protocol'] == 'TCP') & df['Flags'].notna()]
    # Calculate the distribution of each flag as a percentage of total TCP
    flag_counts = df['Flags'].value_counts(normalize=True) * 100
    plt.figure(figsize=(8, 8))
    plt.pie(flag_counts, labels=flag_counts.index, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title(f"{label} - Flags Distribution as Percentage of TCP Traffic")
    plt.show()
