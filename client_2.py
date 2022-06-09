import socket

PORT = 0
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = '!DISCONNECT'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
