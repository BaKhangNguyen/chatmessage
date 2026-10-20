import socket
ip = input("Server IP: ")
chat = socket.socket()
chat.connect((ip, 5001))

print("Connected to Bro!")

while True:
    message = chat.recv(1024).decode()
    if not message or message == "/quit":
        break
    print("Friend:", message)

    reply = input("You: ")
    chat.sendall(reply.encode())
    if reply == "/quit":
        break

chat.close()
