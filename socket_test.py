import socket

#Optional: set timeout to avoid hanging
s= socket.socket
#Socket.py

s.settimeout(1)  #seconds

# Try connecting to loalhost on port 80
result= s.connect_ex(("localhost", 443))

# Print result
print("port open" if result== 0 else "port closed")
s. closed()
