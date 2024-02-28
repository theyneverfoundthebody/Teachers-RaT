# Student Program

import socket
import os

# Define the server's IP address and port
SERVER_HOST = '127.0.0.1'  # Change this to the teacher's IP address
SERVER_PORT = 65432

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the teacher's control program
    s.connect((SERVER_HOST, SERVER_PORT))

    # Communication loop
    while True:
        # Receive command from the teacher
        command = s.recv(1024).decode()

        if command == 'shutdown':
            # Shutdown the computer
            os.system('shutdown /s /t 1')
        elif command == 'restart':
            # Restart the computer
            os.system('shutdown /r /t 1')
        else:
            print("Invalid command")
