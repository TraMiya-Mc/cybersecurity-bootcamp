import re 
log = "Error from 192.168.1.1"
ip_address = re.search(r'\d+\.\d+\.\d+\.\d+', log)

if ip_address:
    print("IP:", ip_address.group())
else: 
    print("No IP found")