import pandas as pd
import matplotlib.pyplot as plt

file_paths = [
    'zoom.csv',
    'youtube.csv',
    'spotify.csv',
    'google.csv',
    'edge.csv'
]
file_labels = ['Zoom', 'YouTube', 'Spotify', 'Google', 'Edge']
avg_packets_per_second = []
for file in file_paths:
    df = pd.read_csv(file)
    df['Time'] = pd.to_datetime(df['Time'], unit='s')
    # Group by each second and count packets in each group
    packets_per_second = df.groupby(df['Time'].dt.floor('s')).size()
    # Calculate average packets per second and append to list
    avg_packets_per_second.append(packets_per_second.mean())

plt.figure(figsize=(10, 6))
plt.bar(file_labels, avg_packets_per_second, color='teal')
plt.xlabel('Services')
plt.ylabel('Average Packets per Second')
plt.title('Comparison of Average Packets per Second Across Services')
plt.xticks(rotation=45)
plt.show()
