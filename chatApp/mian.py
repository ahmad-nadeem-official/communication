import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345

print(f"Hostname: {HOST}")
print(f"Local IP Address: {PORT}")

hostname = socket.gethostname()

# Get the IP address of the local machine
local_ip = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"Local IP Address: {local_ip}")