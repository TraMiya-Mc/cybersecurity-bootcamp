import csv 
import os

# use a file in the same as the script
file_path = r"C:\Users\Tramiya\cybersecurity-bootcamp\Security_logs.csv"

# check if file exists
if not os.path.exists(file_path):
    print(f"Error: {file_path} not found in folder!")
else:
    # Open the CSV file
    with open(file_path, newline='', encoding="utf-8-sig") as f:
        reader= csv.DictReader(f)
        print("Failed login attempts (Event ID 4625):\n")

        # Go through each row and check for Event ID 4625
        found = False
        for row in reader:
            if row.get("EventID") == "4625":
                time = row.get("TimeCreated") or row.get("Date")
                user = row.get("Account Name") or row.get("User")
                print(f"Time: {time} | User: {user}")
                found = True 

