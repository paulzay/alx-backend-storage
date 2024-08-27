#!/usr/bin/env python3
""" 12. Log stats """
from pymongo import MongoClient


def get_nginx_stats():
    """ provides some stats about Nginx logs stored in MongoDB """
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Get total number of logs
    total_logs = collection.count_documents({})

    # Get count of each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({
        "method": method}) for method in methods}

    # Get count of GET requests with path=/status
    status_check = collection.count_documents({
        "method": "GET", "path": "/status"})

    # Display results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    get_nginx_stats().nginx
