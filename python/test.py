import os
import time
from cassandra.cluster import Cluster

def connect_to_cassandra():
    try:
        cluster = Cluster(['cassandra'])
        session = cluster.connect()
        return session
    except Exception as e:
        print(f"Error connecting to Cassandra: {e}")
        return None

def transfer_data(session):
    print("Transferring data to Cassandra...")

    # Create a keyspace and table if they don't exist
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS mykeyspace
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
    """)
    session.execute("""
        CREATE TABLE IF NOT EXISTS mykeyspace.mytable (
            id int,
            name text,
            PRIMARY KEY (id)
        );
    """)

    # Insert some sample data
    session.execute("INSERT INTO mykeyspace.mytable (id, name) VALUES (%s, %s)", (1, "John Doe"))
    session.execute("INSERT INTO mykeyspace.mytable (id, name) VALUES (%s, %s)", (2, "Jane Doe"))

def main():
    session = connect_to_cassandra()
    while session is None:
        print("Retrying connection to Cassandra...")
        time.sleep(5)
        session = connect_to_cassandra()

    transfer_data(session)

    # Close Cassandra connection
    session.shutdown()

if __name__ == "__main__":
    main()