import socket
import sys
import chatbot as cb

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
while True:
    clientSocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientSocket.send(bytes("Hello there!", "utf-8"))
    while True:
        data = clientSocket.recv(1024)
        if not data:
            sys.exit()
        replay = cb.res(data.decode("utf-8"))
        clientSocket.sendall(replay.encode("utf-8"))
clnt.close()
