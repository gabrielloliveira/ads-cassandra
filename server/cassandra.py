import uuid

from cassandra.cluster import Cluster, PlainTextAuthProvider
from decouple import config

HOST = config("HOST")
class CassandraDriver:
    def __init__(self):
        self.auth_provider = PlainTextAuthProvider(username=config("DATABASE_USERNAME"), password=config("DATABASE_PASSWORD"))
        self.cluster = Cluster([HOST], auth_provider=self.auth_provider)
        self.create_tables()
        self.session = self.cluster.connect("files")


    def create_tables(self):
        session = self.cluster.connect()
        session.execute("CREATE KEYSPACE IF NOT EXISTS files WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };")
        session.execute("CREATE TABLE IF NOT EXISTS files.file ( id UUID PRIMARY KEY, name text, data blob, );")
        session.shutdown()


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
