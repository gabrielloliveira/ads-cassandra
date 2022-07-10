import uuid

from cassandra.cluster import Cluster, PlainTextAuthProvider
from decouple import config

# TODO: Implementar verificação se a tabela existe. caso não exista, executar os comandos que estão no arquivo script.sql
# TODO: Setar o host dentro do cluster: Cluster([host], auth_provider=self.auth_provider)


class CassandraDriver:
    def __init__(self):
        self.auth_provider = PlainTextAuthProvider(username=config("DATABASE_USERNAME"), password=config("DATABASE_PASSWORD"))
        self.cluster = Cluster(auth_provider=self.auth_provider)
        self.session = self.cluster.connect("files")

    def all(self):
        return self.session.execute("SELECT * FROM files.file")

    def create(self, file_data):
        name = f"{uuid.uuid4().hex}.txt"
        self.session.execute(
            """
            INSERT INTO files.file (id, name, data)
            VALUES (%s, %s, %s)
            """,
            (uuid.uuid4(), name, file_data),
        )
