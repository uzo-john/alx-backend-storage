#!/usr/bin/env python3
'''Task 8's module.
'''


def list_all(mongo_collection):
    return [doc for doc in mongo_collection.find()]
