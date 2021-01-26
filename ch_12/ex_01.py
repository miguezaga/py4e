import socket
#http://data.pr4e.org/romeo.txt

try:
    webpage = input("Enter - ")
    hostname = webpage.split('/')[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((hostname, 80))
    cmd = (('GET %s HTTP/1.0\r\n\r\n') % webpage).encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()

except:
    print("Wrong URL")
