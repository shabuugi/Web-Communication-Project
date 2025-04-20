# this code will provide an histogram that shows the differences between all the services by the flow volume of the bits


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
total_bytes = []
# counting the bytes in each file
for file in file_paths:
    df = pd.read_csv(file)
    total_sum = df['Length'].sum()
    total_bytes.append(total_sum)

plt.figure(figsize=(10, 6))
plt.bar(file_labels, total_bytes, color='purple')
plt.xlabel('Services')
plt.ylabel('Total Bytes')
plt.title('Comparison of Total Bytes Across Services')
plt.xticks(rotation=45)  # Rotate labels for better visibility
plt.show()
