#!/usr/env python3
# JOKENPO USING SOCKET AND THE PYTHON PROGRAMMING LANGUAGE
# AUTHORS: Felipe de Sousa Rocha, Matheus Oliveira, Caio

import socket
import random

# Server host and port
HOST = 'localhost' # Identifica o nome do servidor
PORT = 5000 # Identifica a porta do servidor
addr = (HOST, PORT)

# List with possible moves that can be chosen by the server
opcoesJogadas = ['Pedra', 'Papel', 'Tesoura']

# The Socket mechanism was created to receive the connection, where in the function we pass 2 arguments, AF_INET which declares the protocol family;
# If it was a transmission via Bluetooth, for example, it would be: AF_BLUETOOTH, and the SOCKET_STREAM, indicates that it will be TCP/IP.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM TCP ID
# The AF_INET constant is part of a group called address families, which are exactly the first optional parameter of the socket constructor.
# AF_INET covers IPv4 addresses, the old Internet standard.

# This line defines which IP and port the server should wait for the connection.
sock.bind(addr)

# Sets the connection limit. And in this case, we are limiting to 5 connections.
sock.listen(5)

print("Aguardando a conexão de um Cliente:")

# Connection and address
conn, ender = sock.accept()

# Presentation of the client's address, composed of the host name and the port that were connected.
print('Connectado com', ender)
print("\nOs palpites do servidor são ALEATÓRIOS!\n")

# The server is released indefinitely or until the connection is closed.
    # Waits for data sent over the network of up to 1024 Bytes, the 'recv' function has only 1 argument which is the size of the Buffer.
while True:
    # 1024 Byter will be received from client
    data = conn.recv(1024)

    # print("Resposta do cliente:", data.decode())

    if not data:

        # When there is nothing else in the data, the connection is closed
        print("\nConexão encerrada!\n")

        # Serves to close the connection between applications.
        conn.close()
        break

    # Used to decode and transform the message into a string sent by the client.
    palpiteClient = str(data.decode())
    # The server guess is chosen at random, the options are inside the Playedoptions list.
    palpiteServ = random.choice(opcoesJogadas)

    # Display server guess
    print("* O Servidor respondeu:", palpiteServ)


    # Check when the client wins the move
    if (palpiteClient == 'Tesoura' and palpiteServ == 'Papel'):
      result = r"""\
    Você	    Máquina
    _    _
   (_)  / )       _____
     | (_/       O_____O
    _+/          /     /
   //|\\        /____ /
  // ||        O_____O
 (/  |/
   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬
   └┐┌┘├┤ ││││  ├┤ │ │
    └┘ └─┘┘└┘└─┘└─┘└─┘"""
    elif (palpiteClient == 'Pedra' and palpiteServ == 'Tesoura'):
      result = r"""\
    Você	    Máquina
                  _    _
    ____         (_)  / )
  _/  _ \\         | (_/
 / _ - _ \\       _+/
 \\_______/      //|\\
                // ||
               (/  |/
   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬
   └┐┌┘├┤ ││││  ├┤ │ │
    └┘ └─┘┘└┘└─┘└─┘└─┘"""

    elif (palpiteClient == 'Papel' and palpiteServ == 'Pedra'):
        result = r"""\
    Você	     Máquina
    _____         ____
   O_____O      _/  _ \\
   /     /     / _ - _ \\
  /____ /      \\_______/
 O_____O
   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬
   └┐┌┘├┤ ││││  ├┤ │ │
    └┘ └─┘┘└┘└─┘└─┘└─┘"""

    elif (palpiteClient == 'Papel' and palpiteServ == 'Tesoura'):
    	result = r"""\
    Você	    Máquina
                  _    _
    _____        (_)  / )
   O_____O         | (_/
   /     /        _+/
  /____ /        //|\\
 O_____O        // ||
               (/  |/
   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬
   ├─┘├┤ ├┬┘ ││├┤ │ │
   ┴  └─┘┴└──┴┘└─┘└─┘"""

    elif (palpiteClient == 'Tesoura' and palpiteServ == 'Pedra'):
      result = r"""\
    Você	     Máquina
    _    _
   (_)  / )       ____
     | (_/      _/  _ \\
    _+/        / _ - _ \\
   //|\\       \\_______/
  // ||
 (/  |/
   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬
   ├─┘├┤ ├┬┘ ││├┤ │ │
   ┴  └─┘┴└──┴┘└─┘└─┘"""

    elif (palpiteClient == 'Pedra' and palpiteServ == 'Papel'):
      result = r"""\
    Você	    Máquina
    ____	  _____
  _/  _ \\       O_____O
 / _ - _ \\      /     /
 \\_______/     /____ /
               O_____O

   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬
   ├─┘├┤ ├┬┘ ││├┤ │ │
   ┴  └─┘┴└──┴┘└─┘└─┘ """

    # Check in case of a tie
    elif (palpiteClient == 'Tesoura' and palpiteServ == 'Tesoura'):
	    result = r"""\
     Você	 Máquina
    _    _       _    _
   (_)  / )     (_)  / )
     | (_/        | (_/
    _+/          _+/
   //|\\        //|\\
  // ||        // ||
 (/  |/       (/  |/
   ┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐
   ├┤ │││├─┘├─┤ │ ├┤
   └─┘┴ ┴┴  ┴ ┴ ┴ └─┘ """

    elif (palpiteClient == 'Pedra' and palpiteServ == 'Pedra'):
	    result = r"""\
    Você	    Máquina
    ____	  ____
  _/  _ \\      _/    \\
 / _ - _ \\    / _ - _ \\
 \\_______/    \\_______/
   ┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐
   ├┤ │││├─┘├─┤ │ ├┤
   └─┘┴ ┴┴  ┴ ┴ ┴ └─┘ """

    elif (palpiteClient == 'Papel' and palpiteServ == 'Papel'):
	    result = r"""\
     Você	     Máquina
    _____         _____
   O_____O       O_____O
   /     /       /     /
  /____ /       /____ /
 O_____O       O_____O
   ┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐
   ├┤ │││├─┘├─┤ │ ├┤
   └─┘┴ ┴┴  ┴ ┴ ┴ └─┘ """

    # Return string to the client
    #result = '- Cliente: '+ str(palpiteClient) + '\n - Servidor: ' + str(palpiteServ) + '\n=> GANHADOR: ' + str(ganhador) + '\n' # Concatenation of results, being presented to the client

    # Used to send the result to the client.
    conn.sendall(bytes(str(result), 'utf8'))
