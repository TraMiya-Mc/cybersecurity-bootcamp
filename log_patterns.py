import csv
from collections import defaultdict
def analyze_log_patterns(file_path):
    try:
        user_counts = defaultdict(int)
        with open(file_path, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row.get("EventID") == "4625":
                        user = row.get("AccountName", "Uknown")
                        user_counts[user] += 1
        print("Users with multiple failed logins (>2):")
        for user, count in user_counts.items():
            if count > 2:
                print(f"{user}: {count} failed logins")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
    except Exception as e: 
        print(f"Error: {e}")