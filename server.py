import socket

server = socket.socket()
server.bind(("0.0.0.0", 5001))
server.listen(1)

print("Waiting for connection...")
chat, address = server.accept()
print("Connected to", address[0])

while True:
    message = input("You: ")
    chat.sendall(message.encode())
    if message == "/quit":
        break

    reply = chat.recv(1024).decode()
    if not reply or reply == "/quit":
        break
    print("Friend:", reply)

chat.close()
server.close()
