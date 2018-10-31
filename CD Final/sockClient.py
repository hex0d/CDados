import socket
import pickle

def client_socket(host,port,message):
    try:
        sock = socket.socket()
        sock.connect((host,port))
        message = pickle.dumps(message)
        sock.send(message)
        data = sock.recv(1024)
        if data.decode('utf-8') == 'ok':
            print(data.decode('utf-8'))
            sock.close()
            return 1
        else:
            return 0
    except socket.error as e:
        return str(e)

if __name__ == '__main__':
    client_socket('127.0.0.1',1313,[1,0,0,1])