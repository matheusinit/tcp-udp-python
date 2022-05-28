#!/usr/env python3

from pydoc import cli
from socket import SOCK_STREAM, socket, AF_INET

# Server host and port
host = '127.0.0.1'
port = 3000

# Create TCP connection
tcp_connection = socket(AF_INET, SOCK_STREAM)

# Bind the scoket to address
tcp_connection.bind((host, port))

# The number of connections to reveice
tcp_connection.listen(1)

while True:
  # Accept connection from client (and receive data from client)
  connection, client_addr = tcp_connection.accept()

  print(f"Message received from {client_addr[0]}")

  # Close connection with client
  connection.close()