# this code will provide an histogram that shows the differences between all the services by the average time between packages


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# File paths and labels
file_paths = [
    'zoom.csv',
    'youtube.csv',
    'spotify.csv',
    'edge.csv',
    'google.csv'
]
file_labels = ['Zoom', 'YouTube', 'Spotify', 'Edge', 'Google']
average_inter_arrivals = []
for file_path in file_paths:
    df = pd.read_csv(file_path)
    df['Time'] = pd.to_datetime(df['Time'])
    df.sort_values('Time', inplace=True)
    # Calculate inter-arrival times (in seconds)
    df['InterArrival'] = df['Time'].diff().dt.total_seconds().fillna(0)
    # Calculate the average inter-arrival
    average_inter_arrivals.append(df['InterArrival'].mean())

plt.figure(figsize=(10, 6))
plt.bar(file_labels, average_inter_arrivals, color='skyblue')
plt.xlabel('Service')
plt.ylabel('Average Inter-Arrival Time (seconds)')
plt.title('Comparison of Average Packet Inter-Arrival Times Across Services')
plt.xticks(rotation=45)
plt.show()
