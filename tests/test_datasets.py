import pytest

from loopr.api.dataset.dataset import Dataset
from loopr.client import LooprClient
from tests.testing_helpers import (
    TEST_IMAGE_DATASET_NAME,
    TEST_IMAGE_DATASET_TYPE,
    TEST_PAIRED_DATASET_NAME,
    TEST_PAIRED_DATASET_TYPE,
)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            {
                "dataset_type": TEST_IMAGE_DATASET_TYPE,
                "paired_type": {},
            },
            TEST_IMAGE_DATASET_NAME,
        ),
        (
            {
                "dataset_type": TEST_PAIRED_DATASET_TYPE,
                "paired_type": {"query": "text", "data": "image"},
            },
            TEST_PAIRED_DATASET_NAME,
        ),
    ],
)
def test_dataset_creation(client: LooprClient, test_input, expected, random_generator):
    dataset_name = random_generator
    dataset = client.create_dataset(
        type=test_input["dataset_type"],
        name=dataset_name,
        slug=dataset_name,
        paired_type=test_input["paired_type"],
    )
    assert dataset.dataset_name == dataset_name


def test_dataset_delete(dataset: Dataset):
    delete_response = dataset.delete()
    assert delete_response == {"successful": True}


def test_dataset_listing(client: LooprClient, dataset: Dataset):
    datasets_name = []
    datasets = client.get_datasets()
    for dataset in datasets:
        datasets_name.append(dataset.dataset_name)
    dataset.delete()
    assert dataset.dataset_name in datasets_name


def test_dataset_add_row(dataset: Dataset):
    row = dataset.add_row(
        type=TEST_IMAGE_DATASET_TYPE,
        data={
            "image_url": "gs://loopr-dev-payloads/a7e9b922-f8d5"
            "-43aa-abb9-5a3095f88edc"
        },
    )
    dataset.delete()
    assert row.successful == True
