import socket

url = input('Enter url: ')
try:
    name = url.split('/')[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((name, 80))
    cmd =('GET '+url+' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
except:
    print("Please enter valid URL: ")
    quit()
count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    count = count + len(data)
    print(data.decode(),end='')
print(count)
