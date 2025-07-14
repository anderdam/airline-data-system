from typing import List

from pymongo import MongoClient


def get_mongo_client(uri: str = "mongodb://localhost:27017") -> MongoClient:
    return MongoClient(uri)


def insert_documents(collection, docs: List[dict]) -> None:
    if docs:
        collection.insert_many(docs)


def find_documents(collection, query=None, projection=None) -> List[dict]:
    if projection is None:
        projection = {}
    if query is None:
        query = {}
    return list(collection.find(query, projection))


def document_exists(collection, filter: dict) -> bool:
    return collection.count_documents(filter) > 0


def create_unique_index(collection, field: str) -> None:
    collection.create_index(field, unique=True)
