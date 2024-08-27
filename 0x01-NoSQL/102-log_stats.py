#!/usr/bin/env python3
""" Log stats- new version """
from pymongo import MongoClient


def log_stats(mongo_collection, option=None):
    """ provides some stats about Nginx logs stored in MongoDB """
    if option is None:
        return mongo_collection.estimated_document_count()
    if option == "method":
        return mongo_collection.count_documents({})
    return mongo_collection.count_documents(option)
