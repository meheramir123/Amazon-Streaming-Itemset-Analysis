import pandas as pd
import json

def read_json_file(file_path='/home/mehar/Downloads/assignment/preprocessed_data.json'):
    """Reads and loads JSON data from a file."""
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file if line.strip()]
    return data

def process_json(data):
    """Process JSON data to DataFrame."""
    df = pd.json_normalize(data, sep='_')

    # Columns to drop
    columns_to_drop = ['imageURL', 'imageURLHighRes', 'tech1', 'tech2', 'description', 'similar']
    df = df.drop(columns=columns_to_drop, errors='ignore')

    # Convert lists to strings if needed
    df['also_buy'] = df['also_buy'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
    df['also_viewed'] = df['also_viewed'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
    df['categories'] = df['categories'].apply(lambda x: ' > '.join(sum(x, [])) if isinstance(x, list) else x)

    return df

path = '/home/mehar/Downloads/assignment/preprocessed_data.json'  # Corrected file path
data = read_json_file(path)
df = process_json(data)
print(df.head())
