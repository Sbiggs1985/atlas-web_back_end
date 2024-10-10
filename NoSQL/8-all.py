#!/usr/bin/env python3
def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    :param mongo_collection: The pymongo collection object
    :return: A list of all documents, or an empty list if no documents exist
    """
    # Retrieve all documents from the collection
    documents = mongo_collection.find()

    # Return a list of documents, or an empty list if no documents are found
    return
