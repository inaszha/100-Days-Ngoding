import numpy as np

# Data awal
data = {
    'x1': [641.87, 637.17, 591.16, 578.47, 556.3, 547.23, 438.08, 364.66, 359.69, 242.03, 190.68, 179.43],
    'x2': [64.13, 63.763, 63.377, 62.525, 62.054, 61.553, 60.484, 59.93, 59.375, 58.29, 57.271, 56.784],
    'x3': [55.596, 54.1971, 52.7121, 49.428, 47.7306, 46.1315, 43.493, 42.4628, 41.5105, 39.2952, 36.2725, 34.6181],
    'x4': [3.55, 3.419, 2.942, 2.494, 2.47, 1.984, 1.725, 1.692, 1.679, 1.634, 1.559, 1.128]
}

# Melakukan normalisasi untuk setiap kolom
normalized_data = {}

for column_name, column_data in data.items():
    min_value = min(column_data)
    max_value = max(column_data)
    normalized_column = [(x - min_value) / (max_value - min_value) for x in column_data]
    normalized_data[column_name] = normalized_column

# Menampilkan hasil normalisasi
for column_name, column_data in normalized_data.items():
    print(f"{column_name}: {column_data}")
