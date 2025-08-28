import socket
host = "localhost"
ports = [80, 443]

for port in ports:
    sock = socket.(socket.AF_INET,socket.SOCK_STREAM)
sock.settimeout(1) #Wait 1 Second
result = sock.connect_ex((host, port))

if result == 0:
    print(f"check Port {port} is OPEN on {host}")
else:
    print(f"Port {port} is CLOSED on {host}")

sock.close()