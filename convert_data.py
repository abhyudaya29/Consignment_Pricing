import csv
import json

csv_file_path = "notebook\data\SCMS_Delivery_History_Dataset.csv"
json_file_path = "data.json"

# Read CSV and convert to JSON
csv_data = []
with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        csv_data.append(row)

# Write JSON data to a file
with open(json_file_path, "w") as json_file:
    json.dump(csv_data, json_file, indent=4)

print(f"CSV file '{csv_file_path}' converted to JSON file '{json_file_path}'")
