import socket
thesock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
thesock.connect(('data.pr4e.org', 80))
req = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
thesock.send(req)

while True:
    data = thesock.recv(512)
    if len(data) < 1:
        break
    print(data)
thesock.close()
