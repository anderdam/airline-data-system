import unittest
from unittest.mock import MagicMock, patch

from src.data_ingestion.get_raw_data import GetRawData


class TestGetRawData(unittest.TestCase):

    @patch("src.data_ingestion.get_raw_data.insert_documents")
    @patch("src.data_ingestion.get_raw_data.get_mongo_client")
    @patch("requests.get")
    def test_fetch_all_with_empty_response_does_nothing(
        self, mock_get, mock_client, mock_insert
    ):
        """
        Simulates an API response with empty 'data' and checks that no insert is attempted.
        """
        mock_get.return_value.json.return_value = {"data": []}

        mock_collection = MagicMock()
        mock_collection.count_documents.return_value = 0
        mock_client.return_value = {
            "airline_data_system": {"aviationstack": mock_collection}
        }

        fetcher = GetRawData("aviationstack", "https://api.mock")
        fetcher.fetch_all()

        mock_insert.assert_not_called()
        mock_get.assert_called_once()

    @patch("src.data_ingestion.get_raw_data.insert_documents")
    @patch("src.data_ingestion.get_raw_data.get_mongo_client")
    @patch("requests.get")
    def test_fetch_all_stops_on_short_page(self, mock_get, mock_client, mock_insert):
        """
        Mocks an API response with fewer than 'limit' items and ensures only one call is made.
        """
        sample_data = {"data": [{"airport_id": str(i)} for i in range(3)]}
        mock_get.return_value.json.return_value = sample_data

        mock_collection = MagicMock()
        mock_collection.count_documents.return_value = 0
        mock_client.return_value = {
            "airline_data_system": {"aviationstack": mock_collection}
        }

        fetcher = GetRawData("aviationstack", "https://api.mock")
        fetcher.fetch_all()

        mock_insert.assert_called_once_with(mock_collection, sample_data["data"])
        mock_get.assert_called_once()

    @patch("src.data_ingestion.get_raw_data.insert_documents")
    @patch("src.data_ingestion.get_raw_data.get_mongo_client")
    @patch("requests.get")
    def test_fetch_all_inserts_data_correctly(self, mock_get, mock_client, mock_insert):
        """
        Simulates two pages: one full page and one empty, and verifies correct insertion.
        """
        full_page = {"data": [{"airport_id": str(i)} for i in range(100)]}
        empty_page = {"data": []}
        mock_get.side_effect = [
            MagicMock(json=lambda: full_page),
            MagicMock(json=lambda: empty_page),
        ]

        mock_collection = MagicMock()
        mock_collection.count_documents.return_value = 0
        mock_client.return_value = {
            "airline_data_system": {"aviationstack": mock_collection}
        }

        fetcher = GetRawData("aviationstack", "https://api.mock")
        fetcher.fetch_all()

        mock_insert.assert_called_once_with(mock_collection, full_page["data"])
        self.assertEqual(mock_get.call_count, 2)


if __name__ == "__main__":
    # Run the tests
    unittest.main()
