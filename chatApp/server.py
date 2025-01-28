import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()


clients = []
nicknames = []

#broadcasting
def broadcasting (message):
    for client in clients:
        client.send(message)

#handleing indiviuas
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]} : {message.decode('utf-8')}")
            broadcasting(message)
        except :
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcasting(f'{nickname} has left the chat !'.encode('utf-8'))
            nicknames.remove(nickname)
            break

#accepting the connection
def recieve_connection():
    print("server is running ....")
    while True:
        client , address = server.accept()
        print(f"new connection {str(address)}")
        client.send('NICK'.encode('utf-8')) #send the nickname
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print(f'Nickname of the client is {nickname}!')
        print(f'Number of clients connected {len(clients)}')
        client.send('Connected to the server !'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        recieve_connection()  #start the server

