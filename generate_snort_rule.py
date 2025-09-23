# generate_snort_rule.py
try:
    rules = [
        'alert tcp any any -> 80 (msg:"HTTP traffic detected"; sid:1000001; rev;1;)'
        'alert tcp any any -> 443 (msg:"HTTPS traffic detected"; sid:1000002; rev:1;)'
    ]

    with open("snort_rule.rules", "w") as f:
        for rule in rules:
            f.write(rule + "\n")
            print(rule)

    print("Rules saved to snort_rule.rules")

except Exception as e:
    print("Error", e)