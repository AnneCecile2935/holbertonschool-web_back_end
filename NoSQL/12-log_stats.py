#!/usr/bin/env python3
"""
12-log_stats.py

Display statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    # Total number of logs
    total = nginx.count_documents({})
    print("{} logs".format(total))

    # Methods statistics
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for m in methods:
        count = nginx.count_documents({"method": m})
        print("\tmethod {}: {}".format(m, count))

    # GET /status requests
    status = nginx.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status))
