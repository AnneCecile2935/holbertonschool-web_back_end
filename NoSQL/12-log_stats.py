#!/usr/bin/env python3
"""
12-log_stats.py

Display statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

if __name__ == "__main__":
    # Connexion à MongoDB et accès à la collection nginx
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Nombre total de logs
    x_logs = nginx_collection.count_documents({})
    print(f"{x_logs} logs")

    # Statistiques par méthode
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Nombre de requêtes GET sur /status
    status_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_count} status check")
