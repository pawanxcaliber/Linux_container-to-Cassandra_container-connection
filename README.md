Here's a detailed README for your GitHub repository:
DevOps Project: Cassandra and Python Containers
Overview
This project demonstrates a simple DevOps setup using Docker containers. It consists of two main components:
A Cassandra database container
A Python application container that interacts with the Cassandra database
Prerequisites
Docker installed on your system
Docker Compose installed on your system
Getting Started
Step 1: Clone the Repository
Clone this repository to your local machine:
Bash
git clone https://github.com/your-username/your-repo-name.git
Step 2: Build and Start the Containers
Navigate to the project directory and build the Docker images:
Bash
docker-compose build
Start the containers:
Bash
docker-compose up
Step 3: Verify the Containers
Check the status of the containers:
Bash
docker-compose ps -a
This should display both the Cassandra and Python containers running.
Cassandra Database
Accessing the Cassandra Database
Enter the Cassandra container:
Bash
sudo docker-compose exec cassandra bash
Start the CQLSH tool:
Bash
cqlsh
Creating a Keyspace and Table
Create a keyspace:
SQL
CREATE KEYSPACE mykeyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
Create a table:
SQL
CREATE TABLE mykeyspace.mytable (id int, name text, PRIMARY KEY (id));
Inserting Data
Insert some sample data:
SQL
INSERT INTO mykeyspace.mytable (id, name) VALUES (1, 'John Doe');
INSERT INTO mykeyspace.mytable (id, name) VALUES (2, 'Jane Doe');
Querying Data
Query the data:
SQL
SELECT * FROM mykeyspace.mytable;
This should display the inserted data.
Python Application
Overview
The Python application container interacts with the Cassandra database. It uses the cassandra-driver library to connect to the Cassandra database.
Code
The Python code is located in the python directory. It consists of a simple script that connects to the Cassandra database and inserts some sample data.
Troubleshooting
Make sure Docker and Docker Compose are installed and running correctly.
Check the Docker container logs for any errors.