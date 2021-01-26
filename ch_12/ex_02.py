import socket
#http://data.pr4e.org/romeo.txt
#http://data.pr4e.org/romeo-full.txt

try:
    webpage = input("Enter - ")
    hostname = webpage.split('/')[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((hostname, 80))
    cmd = (('GET %s HTTP/1.0\r\n\r\n') % webpage).encode()
    mysock.send(cmd)

    txt = b""

    char_count = 0
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break

        char_count += len(data)

        if char_count < 3000:
            print(data.decode(),end='')


    print(char_count)

    mysock.close()

except:
    print("Wrong URL")
