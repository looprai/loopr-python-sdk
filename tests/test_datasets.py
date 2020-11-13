import pytest
from loguru import logger

from loopr.api.dataset.dataset import Dataset
from loopr.client import LooprClient
from loopr.exceptions import LooprInvalidResourceError
from tests.testing_helpers import (
    PREDICTIONS,
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

    @pytest.mark.parametrize(
        "test_input",
        [
            (
                {
                    "dataset_type": TEST_IMAGE_DATASET_TYPE,
                    "data": {"image_url": "gs://loopr-dev-payloads/a7e9b922-f8d5"},
                },
            ),
            (
                {
                    "dataset_type": TEST_IMAGE_DATASET_TYPE,
                    "data": {
                        "image_url": "gs://loopr-dev-payloads/a7e9b922-f8d5"
                        "-43aa-abb9-5a3095f88edc",
                        "predictions": PREDICTIONS,
                    },
                },
            ),
        ],
    )
    def test_dataset_add_row_and_delete(self, dataset: Dataset, test_input):
        row = dataset.add_row(
            type=test_input[0]["dataset_type"],
            data=test_input[0]["data"],
        )
        dataset.delete_rows([row.uid])
        assert row.dataset_id == dataset.uid

    @pytest.mark.parametrize(
        "test_input",
        [
            (
                {
                    "dataset_type": TEST_PAIRED_DATASET_TYPE,
                    "data": {"image": "gs://loopr-dev-payloads/a7e9b922-f8d5"},
                    "query": {"text": "HELLO"},
                },
            ),
        ],
    )
    def test_dataset_add_row_paired_and_delete(
        self, dataset_paired: Dataset, test_input
    ):
        row = dataset_paired.add_row(
            type=test_input[0]["dataset_type"],
            data=test_input[0]["data"],
            query=test_input[0]["query"],
        )
        dataset_paired.delete_rows([row.uid])
        assert row.dataset_id == dataset_paired.uid
