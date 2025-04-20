import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_paths = [
    'zoom.csv',
    'youtube.csv',
    'spotify.csv',
    'edge.csv',
    'google.csv'
]
file_labels = ['Zoom', 'YouTube', 'Spotify', 'Edge', 'Google']



averages = []

for file in file_paths:
    df = pd.read_csv(file)
    average = df['Length'].mean()
    averages.append(average)

fig, ax = plt.subplots()
index = np.arange(5)
bar_width = 0.35
bars = plt.bar(index, averages, bar_width, label='Average Packet Size')
plt.xlabel('Services')
plt.ylabel('Packet Size')
plt.title('Comparison of Average Packet Size')
plt.xticks(index, file_labels)
plt.legend()
plt.tight_layout()
plt.show()
