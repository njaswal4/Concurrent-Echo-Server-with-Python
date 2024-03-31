# Concurrent Echo Server with Python

## Overview
In this project, we implement a concurrent echo server in Python using sockets and threading. The server listens for incoming connections from clients and echoes back any messages it receives. Clients can connect to the server, send messages, and receive responses.

## Requirements
- Python 3.x

## Server Implementation
- `server.py`: Python script for the server.
  - Binds to localhost and a chosen port.
  - Utilizes threading to handle multiple client connections concurrently.
  - Echoes messages back to clients and handles "quit" messages to close connections gracefully.

## Client Implementation
- `client.py`: Python script for the client.
  - Connects to the server using TCP.
  - Sends messages to the server and displays responses.
  - Handles "quit" message to close the connection.

## Instructions
1. Start the server by running `python Server.py`.
2. Start a client by running `python Client.py`.
3. Enter messages in the client's terminal to send to the server.
4. Enter "quit" to exit the client and close the connection.

## Assessment Criteria
- Functionality: The server can handle multiple client connections concurrently and echoes messages correctly.
- Robustness: Both server and client handle potential errors gracefully.
- Code Quality: Well-organized, commented, and follows Pythonic conventions.
