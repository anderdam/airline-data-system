import unittest

from mongomock import MongoClient

from src.storage_commons.mongodb_utils import (
    create_unique_index,
    document_exists,
    find_documents,
    insert_documents,
)


class TestMongoUtils(unittest.TestCase):

    def setUp(self):
        """
        Sets up an in-memory MongoDB using mongomock for each test.
        """
        client = MongoClient()
        self.collection = client["test_db"]["test_collection"]

    def test_insert_documents_only_adds_non_empty(self):
        """
        Verifies insert_documents ignores empty lists and adds valid documents.
        """
        insert_documents(self.collection, [])
        self.assertEqual(self.collection.count_documents({}), 0)

        insert_documents(self.collection, [{"airport_id": "1"}])
        self.assertEqual(self.collection.count_documents({}), 1)

    def test_find_documents_returns_expected_fields(self):
        """
        Tests the projection of fields using find_documents.
        """
        insert_documents(self.collection, [{"airport_id": "1", "country": "BR"}])
        docs = find_documents(self.collection, projection={"airport_id": 1, "_id": 0})

        self.assertEqual(len(docs), 1)
        self.assertIn("airport_id", docs[0])
        self.assertNotIn("country", docs[0])
        self.assertNotIn("_id", docs[0])

    def test_create_unique_index_blocks_duplicates(self):
        """
        Ensures that unique indexes throw errors on duplicate inserts.
        """
        create_unique_index(self.collection, "airport_id")
        insert_documents(self.collection, [{"airport_id": "1"}])

        with self.assertRaises(Exception):
            insert_documents(self.collection, [{"airport_id": "1"}])  # Duplicate key

    def test_document_exists_returns_true_when_found(self):
        """
        Confirms that document_exists correctly identifies existing entries.
        """
        insert_documents(self.collection, [{"airport_id": "1"}])
        self.assertTrue(document_exists(self.collection, {"airport_id": "1"}))
        self.assertFalse(document_exists(self.collection, {"airport_id": "XYZ"}))


if __name__ == "__main__":
    unittest.main()
