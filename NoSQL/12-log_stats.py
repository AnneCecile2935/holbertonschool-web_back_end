#!/usr/bin/env python3
"""
12-log_stats.py

Module to display statistics about Nginx logs stored in MongoDB.

It connects to the 'logs' database and the 'nginx' collection, then prints:
1. The total number of logs.
2. The number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE).
3. The number of GET requests to the path '/status'.
"""


from pymongo import MongoClient


def main():
    """
    Connects to MongoDB and prints Nginx log statistics.

    Steps performed:
    1. Connects to the local MongoDB server.
    2. Accesses the 'logs' database and 'nginx' collection.
    3. Counts the total number of documents in the collection.
    4. Counts the number of documents per HTTP method:
       GET, POST, PUT, PATCH, DELETE.
    5. Counts the number of GET requests to '/status'.
    6. Prints all statistics in a formatted manner.
    """
    #  connexion à MongoDB, à la base logs et la collection nginx
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Nombre total de logs
    x_logs = nginx_collection.count_documents({})
    print(f"{x_logs} logs")

    # Statistiques par méthode
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    # Nombre de requêtes GET sur /status
    status_count = (
        nginx_collection.count_documents({"method": "GET", "path": "/status"})
    )
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()
