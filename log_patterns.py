import csv, 
from collections import defaultdict

def log_patterns(file_path
    try:
        with open(file_path, "r") as p:
                reader = csv.DictReader(p)
                failed_logins = {
                for row in reader:
                    if row.get("EventID") == "4625":
                        username = row.get("AccountName", Uknown")
                        if failed_logins > 1:
                            print(f"User: {username}, {failed_logins},")
    except FileNotFoundError:
    print(f"Error: File {file_path})
