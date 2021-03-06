from time import sleep

import pytest

from loopr.api.dataset.dataset import Dataset
from loopr.client import LooprClient
from loopr.exceptions import LooprInvalidResourceError
from tests.testing_helpers import (
    TEST_IMAGE_DATASET_TYPE,
    TEST_INVALID_DATASET_ID,
    TEST_SKU_DATASET_TYPE,
    TEST_TEXT_DATASET_TYPE,
    random_generator,
)


@pytest.mark.usefixtures("dataset", "dataset_text", "dataset_sku")
class TestDataset:
    @pytest.mark.parametrize(
        "test_input",
        [
            (
                {
                    "dataset_type": TEST_IMAGE_DATASET_TYPE,
                },
            ),
            (
                {
                    "dataset_type": TEST_TEXT_DATASET_TYPE,
                },
            ),
            (
                {
                    "dataset_type": TEST_SKU_DATASET_TYPE,
                },
            ),
        ],
    )
    def test_dataset_creation_deletion(self, client: LooprClient, test_input):
        dataset_name = "test-dataset-" + random_generator()
        dataset = client.create_dataset(
            dataset_type=test_input[0]["dataset_type"],
            dataset_name=dataset_name,
            dataset_slug=dataset_name,
        )
        dataset.delete()
        assert dataset.uid == dataset.to_dict()["uid"]
        assert dataset.dataset_name == dataset_name
        sleep(2)
        with pytest.raises(LooprInvalidResourceError):
            client.create_dataset(
                dataset_type="invalid_type",
                dataset_name=dataset_name,
            )
        sleep(2)
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
                    "data": {
                        "image": "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d",
                    },
                },
            ),
            (
                {
                    "dataset_type": TEST_IMAGE_DATASET_TYPE,
                    "data": {
                        "image": "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d",
                    },
                },
            ),
            (
                {
                    "dataset_type": TEST_IMAGE_DATASET_TYPE,
                    "data": {
                        "image": "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d",
                        "query": "query",
                    },
                },
            ),
            (
                {
                    "dataset_type": TEST_IMAGE_DATASET_TYPE,
                    "data": {
                        "image": "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d",
                        "query": "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d",
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

    def test_get_dataset_info_id(self, client: LooprClient, dataset: Dataset):
        response = client.get_dataset(dataset_id=dataset.uid)
        assert response.dataset_name == dataset.dataset_name
        with pytest.raises(LooprInvalidResourceError):
            response = client.get_dataset(dataset_id=TEST_INVALID_DATASET_ID)

    def test_get_dataset_info_slug(self, client: LooprClient, dataset: Dataset):
        response = client.get_dataset(dataset_slug=dataset.dataset_slug)
        assert response.dataset_name == dataset.dataset_name

    def test_get_text_dataset_info_id(self, client: LooprClient, dataset_text: Dataset):
        response = client.get_dataset(dataset_id=dataset_text.uid)
        assert response.dataset_name == dataset_text.dataset_name
        with pytest.raises(LooprInvalidResourceError):
            client.get_dataset(dataset_id="sdgfgueygbabdad")

    def test_get_text_dataset_info_slug(
        self, client: LooprClient, dataset_text: Dataset
    ):
        response = client.get_dataset(dataset_slug=dataset_text.dataset_slug)
        assert response.dataset_name == dataset_text.dataset_name

    def test_get_sku_dataset_info_id(self, client: LooprClient, dataset_sku: Dataset):
        response = client.get_dataset(dataset_id=dataset_sku.uid)
        assert response.dataset_name == dataset_sku.dataset_name
        with pytest.raises(LooprInvalidResourceError):
            client.get_dataset(dataset_id=TEST_INVALID_DATASET_ID)

    def test_get_sku_dataset_info_slug(self, client: LooprClient, dataset_sku: Dataset):
        response = client.get_dataset(dataset_slug=dataset_sku.dataset_slug)
        assert response.dataset_name == dataset_sku.dataset_name

    @pytest.mark.parametrize(
        "test_input",
        [
            (
                {
                    "dataset_type": TEST_TEXT_DATASET_TYPE,
                    "data": {"text": "Sample Text"},
                },
            ),
            (
                {
                    "dataset_type": TEST_TEXT_DATASET_TYPE,
                    "data": {"text": "Sample Text", "query": "query"},
                },
            ),
        ],
    )
    def test_dataset_text_add_row_and_delete(self, dataset_text: Dataset, test_input):
        row = dataset_text.add_row(
            type=test_input[0]["dataset_type"],
            data=test_input[0]["data"],
        )
        dataset_text.delete_rows([row.uid])
        assert row.dataset_id == dataset_text.uid

    @pytest.mark.parametrize(
        "test_input",
        [
            (
                {
                    "dataset_type": TEST_SKU_DATASET_TYPE,
                    "data": {
                        "sku_image": "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d",
                        "sku_name": "Sample Sku Name",
                    },
                },
            ),
            (
                {
                    "dataset_type": TEST_SKU_DATASET_TYPE,
                    "data": {
                        "sku_image": "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d",
                        "sku_name": "Sample Sku Name",
                        "query": "query",
                    },
                },
            ),
            (
                {
                    "dataset_type": TEST_SKU_DATASET_TYPE,
                    "data": {
                        "sku_image": "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d",
                        "sku_name": "Sample Sku Name",
                        "query": "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d",
                    },
                },
            ),
        ],
    )
    def test_dataset_sku_add_row_and_delete(self, dataset_sku: Dataset, test_input):
        row = dataset_sku.add_row(
            type=test_input[0]["dataset_type"],
            data=test_input[0]["data"],
        )
        dataset_sku.delete_rows([row.uid])
        assert row.dataset_id == dataset_sku.uid

    @pytest.mark.parametrize(
        "test_input",
        [
            ({"dataset_name": "updateddataset", "description": None},),
            ({"dataset_name": "updateddataset", "description": "description"},),
            ({"dataset_name": None, "description": "description"},),
        ],
    )
    def test_update_image_dataset(self, dataset: Dataset, test_input):
        response = dataset.update_dataset(
            dataset_name=test_input[0]["dataset_name"],
            description=test_input[0]["description"],
        )
        assert (response["dataset_name"] == test_input[0]["dataset_name"]) or (
            response["description"] == test_input[0]["description"]
        )

    @pytest.mark.parametrize(
        "test_input",
        [
            ({"dataset_name": "updateddataset", "description": None},),
            ({"dataset_name": "updateddataset", "description": "description"},),
            ({"dataset_name": None, "description": "description"},),
        ],
    )
    def test_update_text_dataset(self, dataset_text: Dataset, test_input):
        response = dataset_text.update_dataset(
            dataset_name=test_input[0]["dataset_name"],
            description=test_input[0]["description"],
        )
        assert (response["dataset_name"] == test_input[0]["dataset_name"]) or (
            response["description"] == test_input[0]["description"]
        )

    @pytest.mark.parametrize(
        "test_input",
        [
            ({"dataset_name": "updateddataset", "description": None},),
            ({"dataset_name": "updateddataset", "description": "description"},),
            ({"dataset_name": None, "description": "description"},),
        ],
    )
    def test_update_sku_dataset(self, dataset_sku: Dataset, test_input):
        response = dataset_sku.update_dataset(
            dataset_name=test_input[0]["dataset_name"],
            description=test_input[0]["description"],
        )
        assert (response["dataset_name"] == test_input[0]["dataset_name"]) or (
            response["description"] == test_input[0]["description"]
        )
