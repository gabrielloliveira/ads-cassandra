DROP TABLE IF EXISTS files.file;

CREATE KEYSPACE IF NOT EXISTS files WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

CREATE TABLE files.file (
  id UUID PRIMARY KEY,
  name text,
  data blob,
);