from loopr.api.dataset.dataset import Dataset
from loopr.client import LooprClient
from tests.testing_helpers import TEST_IMAGE_DATASET_TYPE, TEST_PAIRED_DATASET_TYPE


class TestRow:
    def test_delete_row_image(self, client: LooprClient, dataset: Dataset):
        row = dataset.add_row(
            type=TEST_IMAGE_DATASET_TYPE,
            data={"image_url": "gs://loopr-dev-payloads/a7e9b922-f8d5"},
        )
        response = row.delete()
        assert response == "successful"

    def test_delete_row_paired(self, client: LooprClient, dataset_paired: Dataset):
        row = dataset_paired.add_row(
            type=TEST_PAIRED_DATASET_TYPE,
            data={"image": "gs://loopr-dev-payloads/a7e9b922-f8d5"},
            query={"text": "HELLO"},
        )
        response = row.delete()
        assert response == "successful"
