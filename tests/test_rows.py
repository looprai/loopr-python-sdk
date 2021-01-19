from loopr.api.dataset.dataset import Dataset
from loopr.client import LooprClient
from tests.testing_helpers import TEST_IMAGE_DATASET_TYPE


class TestRow:
    def test_delete_row_image(self, client: LooprClient, dataset: Dataset):
        row = dataset.add_row(
            type=TEST_IMAGE_DATASET_TYPE,
            data={"image_url": "gs://loopr-dev-payloads/a7e9b922-f8d5"},
        )
        response = row.delete()
        assert response == "successful"
