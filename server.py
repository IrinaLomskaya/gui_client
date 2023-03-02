import socket

#serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
#serv_sock.bind(('', 5005))
server = socket.socket()
ip = "127.0.0.1"
port = 5557
server.bind((ip, port))
server.listen(10)
#serv_sock.listen(10)

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = server.accept()
    print('Connected by', client_addr)
    name_f = (client_sock.recv(1024)).decode('UTF-8')
    f = open('sent/' + name_f, 'wb')

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        data = client_sock.recv(1024)
        print(data)
        f.write(data)
        if not data:
            # Клиент отключился
            break
        #f.close()
        #client_sock.sendall(data)
    #f = open()
    client_sock.close()

