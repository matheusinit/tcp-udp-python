#!/usr/env python3

from socket import socket, AF_INET, SOCK_STREAM

# Server info
host = '127.0.0.1'
port = 3000

# Create TCP connection
tcp_connection = socket(AF_INET, SOCK_STREAM)

# Host (IP address) and port of server to send message
connect_to = (host, port)

# Make the connection
tcp_connection.connect(connect_to)

print("Sending an message...")

# message "Hello World" in bytes
message = "Hello World".encode()

# Send message
tcp_connection.send(message)

# Close connection
tcp_connection.close()