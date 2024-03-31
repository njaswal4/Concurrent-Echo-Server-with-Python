## Name : Nisarg Jaswal
## Student ID: 116088220 

                              ## Server.py
import socket
import threading

active_connections = []

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    active_connections.append(conn)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode()
        print(f"Received from {addr}: {message}")
        if message.lower() == "quit":
            break
        conn.sendall(data)

    print(f"Connection closed by {addr}")
    active_connections.remove(conn)
    conn.close()

    if not active_connections:
        print("No active connections. Server shutting down...")
        exit()

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 8000
    start_server(HOST, PORT)
