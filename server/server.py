import socket

import psutil
import logging

from .cassandra import CassandraDriver

SERVER_ADDRESS = ("0.0.0.0", 8080)
BUFFER_SIZE = 1024 // 2
FINISHED_MESSAGE = b"DONE"
FILE_COMPLETED = b"COMPLETED"


bd = CassandraDriver()


logging.basicConfig(filename="server.log", encoding="utf-8", level=logging.INFO)


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
        while True:
            conn, client_address = self.sock.accept()
            print("‍💼 Received connection from SERVER...", client_address)
            message = conn.recv(BUFFER_SIZE)
            file_parts = []

            while message:
                if str(message) == str(FINISHED_MESSAGE):
                    print("All Files Received")
                    break

                if str(message) == str(FILE_COMPLETED):
                    print("File Received")
                    file_data = "".join(file_parts)
                    bd.create(file_data=file_data.encode())

                    # CPU AND RAM LOGS
                    cpu_percent = psutil.cpu_percent()
                    ram_percent = psutil.virtual_memory()[2]

                    print("🚀 CPU USAGE %", cpu_percent)
                    print("🚀 RAM USAGE %", ram_percent)
                    logging.info(f"CPU-USAGE={cpu_percent}")
                    logging.info(f"RAM-USAGE={ram_percent}")

                    file_parts = []
                    message = b""
                    conn.send("OK".encode())

                message = message.decode("utf-8")
                file_parts.append(message)
                message = conn.recv(BUFFER_SIZE)

            file_parts = []
            response_data = "OK"
            conn.send(str(response_data).encode())
