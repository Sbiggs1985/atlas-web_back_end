#!/usr/bin/env python3
def update_topics(mongo_collection, name, topics):
    """
    Updates the list of topics for a school document based on the name.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
