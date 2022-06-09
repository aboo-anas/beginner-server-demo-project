import socket
import threading

PORT = 0
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "105.112.162.80"
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = '!DISCONNECT'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"{addr} {msg}")
    conn.close()

def start():
    server.listen(10)
    print(f"[LISTENING] Server is listening on {SERVER} using port {server.getsockname()[1]}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

print(f"[STARTING] server is starting...")
start()
