
#!/usr/env python3
# JOKENPO USING SOCKET AND THE PYTHON PROGRAMMING LANGUAGE
# AUTHORS: Felipe Rocha, Matheus Oliveira e Caio

# Libraries
import socket
import random

# Identification of the client's HOST AND PORT
HOST = '127.0.0.1' # Identifies the name of the client
PORT = 5000 # Identifies the port of the client to communicate with the server

# List with possible moves that can be chosen by the client.
opcoesJogadas = ['Pedra', 'Papel', 'Tesoura']

# The Socket mechanism was created to receive the connection, where in the function we pass 2 arguments, AF_INET which declares the protocol family;
# If it was a transmission via Bluetooth, for example, it would be: AF_BLUETOOTH, and the SOCKET_STREAM, indicates that it will be TCP/IP.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# The AF_INET constant is part of a group called address families, which are exactly the first optional parameter of the socket constructor.
# AF_INET covers IPv4 addresses, the old Internet standard.


# Connect to the server
sock.connect((HOST, PORT)) # Double parentheses because connect has only one parameter.

while True: # The client can make n communications with the server, or until this connection is closed.
    # The user chooses the type of move that will be made, being 1 - Random guess and 2 the user informs a guess, finally if he informs 0 (zero) the connection is closed.
    opcao1 = int(input("\n* Escolha uma opção:\n 1- Palpite aleatório\n 2- Informar um palpite\n 0- Para encerrar.\n -> Opcao: "))

    # If the user chooses option 1, then the guess will be random. This randomness is given according to the Playedoptions list.
    if (opcao1 == 1):
        mensagemEnvioClient = random.choice(opcoesJogadas) # Randomization of the move according to the Playoptions list.

    # If the user chooses option 2, then a menu opens to choose the guess.
    if (opcao1 == 2):
        opcao2 = int(input("\n* Ecolha o palpite:\n 1- Pedra\n 2- Papel\n 3- Tesoura\n -> Opcao: "))

        if (opcao2 == 1):
            mensagemEnvioClient = 'Pedra' # If the user chooses option 1, then the move will be Stone.
        elif (opcao2 == 2):
            mensagemEnvioClient = 'Papel' # If the user chooses option 1, then the move will be Paper.
        elif (opcao2 == 3):
            mensagemEnvioClient = 'Tesoura' # If the user chooses option 1, then the move will be Scissors.

    # If the user informs 0 (zero) when choosing the move, then the connection is closed.
    if (opcao1 == 0):
        print("\nConexão encerrada!\n")
        # Used to close the connection between the two applications.
        sock.close()
        break

    # Used to send data to the server.
    sock.sendall(str.encode(mensagemEnvioClient)) # Send message to server

    print("\n-> Palpite enviado pelo cliente: ", mensagemEnvioClient) # Displays the guess chosen by the client

    # Wait for the return from the server, a data sent by the network of up to 1024 Bytes, the 'recv' function has only 1 argument which is the size of the Buffer.
    data = sock.recv(1024) # Bytes

    # Decodes the message received by the server, capitalizes all the letters and finally this message is displayed.
    print('\n*** Resultado final do jogo: \n', data.decode().upper())