# Control Program (Teacher's computer)

import socket

# Define the IP address and port to listen on
HOST = '127.0.0.1'  # Change this to your IP address
PORT = 65432

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the host and port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()

    print("Waiting for a student to connect...")

    # Accept a connection from a student
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)

        # Communication loop
        while True:
            # Receive command from the teacher
            command = input("Enter command (e.g., 'shutdown', 'restart'): ").strip()
            if not command:
                break

            # Send command to the student
            conn.sendall(command.encode())
