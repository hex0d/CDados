import socket
import pickle
import sys

def server_socket(port):
    host = ''

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.bind((host,port))
    except socket.error as e:
        print(str(e))
    sock.listen(5)
    print("Waiting for Connection")

    while True:
        conn, addr = sock.accept()

        print('Connected to ' + addr[0] + ':' + str(addr[1]))
        data = conn.recv(1024)
        if not data:
            break
        data = pickle.loads(data)
        if type(data) is list:
            conn.send(str.encode('ok'))
        else:
            conn.send(str.encode('error'))

    conn.close()
    return data

if __name__ == '__main__':
    server_socket(1313)
