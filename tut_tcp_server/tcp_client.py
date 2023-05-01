"""Client to connect with the server
"""

import socket
from constant import Constant

def main() -> None:
    """fn to send and receive data from server
    """
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_.connect(Constant.Config.SERVER_ADDRESS)
    while True:
        try:            
            data = input("Please enter the message you would like to send ")
            print("sending data to all")
            socket_.sendall(data.encode())
            data_recved = 0
            data_len_expected = len(data)
            while data_recved < data_len_expected:
                from_server = socket_.recv(Constant.Config.BUFFER_SIZE)
                data_recved += len(from_server)
                print(f"Received data from server {from_server}")
        finally:
            print("closing connection from server")
            socket_.close()



if __name__ == "__main__":
    main()
