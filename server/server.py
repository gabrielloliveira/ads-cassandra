import socket
from tempfile import NamedTemporaryFile

SERVER_ADDRESS = ("0.0.0.0", 80)
BUFFER_SIZE = 1024 * 10


class Server:
    def __init__(self):
        self.address = SERVER_ADDRESS
        self.sock = self.__create_sock()

    def __create_sock(self):
        """
        Create TCP server socket
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(self.address)
        return sock

    def run(self):
        """Run the server."""
        print("🚀 Starting server on mode partner...")
        print(f"🚀 Starting server on address {self.address}...")
        self.listen()

    def listen(self):
        """Listen for connections."""
        self.sock.listen()
        file = NamedTemporaryFile(mode="w+t")
        while True:
            conn, client_address = self.sock.accept()
            print("‍💼 Received connection from SERVER...", client_address)
            message = conn.recv(BUFFER_SIZE)

            while message:
                print("Receiving...")
                file.write(message)
                message = conn.recv(BUFFER_SIZE)

            # TODO: Salvar o arquivo no cassandra
            file.close()
            response_data = "OK"
            conn.send(str(response_data).encode())
