import zipfile
import os

zip_file_path = os.path.join(os.path.dirname(__file__), 'icons/icons_ipma_weather (1).zip')

extract_to_path = os.path.join(os.path.dirname(__file__), 'static/meteo')

os.makedirs(extract_to_path, exist_ok=True)

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)

print("Files extracted successfully to:", extract_to_path)