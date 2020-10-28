import pytest
from loguru import logger

from loopr.api.dataset.dataset import Dataset
from loopr.client import LooprClient
from loopr.exceptions import LooprInvalidResourceError
from tests.testing_helpers import (
    TEST_IMAGE_DATASET_TYPE,
    TEST_PAIRED_DATASET_TYPE,
    random_generator,
)


@pytest.mark.usefixtures("dataset")
class TestDataset:
    @pytest.mark.parametrize(
        "test_input",
        [
            (
                {
                    "dataset_type": TEST_IMAGE_DATASET_TYPE,
                    "paired_type": None,
                },
            ),
            (
                {
                    "dataset_type": TEST_PAIRED_DATASET_TYPE,
                    "paired_type": {"query": "text", "data": "image"},
                },
            ),
        ],
    )
    def test_dataset_creation_deletion(self, client: LooprClient, test_input):

        dataset_name = "test-dataset-" + random_generator()
        logger.info(dataset_name)
        dataset = client.create_dataset(
            type=test_input[0]["dataset_type"],
            name=dataset_name,
            slug=dataset_name,
            paired_type=test_input[0]["paired_type"],
        )
        dataset.delete()
        assert dataset.dataset_name == dataset_name
        with pytest.raises(LooprInvalidResourceError):
            dataset.delete()

    def test_dataset_listing(self, client: LooprClient, dataset: Dataset):
        datasets_name = []
        datasets = client.get_datasets()
        for dataset in datasets:
            datasets_name.append(dataset.dataset_name)
        assert dataset.dataset_name in datasets_name

    def test_dataset_add_row(self, dataset: Dataset):
        row = dataset.add_row(
            type=TEST_IMAGE_DATASET_TYPE,
            data={
                "image_url": "gs://loopr-dev-payloads/a7e9b922-f8d5"
                "-43aa-abb9-5a3095f88edc"
            },
        )
        assert row.dataset_id == dataset.uid
