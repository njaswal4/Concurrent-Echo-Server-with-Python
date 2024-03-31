## Name : Nisarg Jaswal
## Student ID: 116088220 

                              ## Client.py
import socket

def start_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")

        while True:
            message = input("Enter message to send (type 'quit' to exit): ")
            client_socket.sendall(message.encode())

            if message.lower() == "quit":
                print("Closing connection...")
                break

            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 8000
    start_client(HOST, PORT)
