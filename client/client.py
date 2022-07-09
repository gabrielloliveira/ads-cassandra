import socket
import time

SERVER_ADDRESS = ("0.0.0.0", 8080)
BUFFER_SIZE = 1024 * 10


class Client:
    def __init__(self):
        self.server_address = SERVER_ADDRESS

    def send_message(self, message):
        print(f"📩 Sending message with TCP CONNECTION: {message}")
        start_time = time.time()
        message = message.encode("utf-8")
        server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        server.connect(self.server_address)
        server.send(message)
        server.shutdown(socket.SHUT_WR)
        response = server.recv(BUFFER_SIZE)
        message = response.decode("utf-8")
        final_time = time.time() - start_time
        print(f"📨 Received response: {message} in {final_time} seconds")

