#!/usr/bin/env python3
def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on kwargs.
    :param mongo_collection: The pymongo collection object
    """

    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
