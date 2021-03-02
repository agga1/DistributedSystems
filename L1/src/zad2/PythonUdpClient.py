import socket

serverIP = "127.0.0.1"
# --- changed server port to match java udp server
serverPort = 9008
msg = "żółta gęś"

print('PYTHON UDP CLIENT')
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# --- changed encoding
client.sendto(bytes(msg, 'utf-8'), (serverIP, serverPort))




