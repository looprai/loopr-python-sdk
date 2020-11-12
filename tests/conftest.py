import os
from enum import Enum

import pytest

from loopr.client import LooprClient
from tests.testing_helpers import (
    TEST_IMAGE_DATASET_TYPE,
    TEST_OBJECT_DETECTION_PROJECT_CONFIG,
    TEST_OBJECT_DETECTION_PROJECT_TYPE,
    TEST_PAIRED_DATASET_TYPE,
    random_generator,
)


class Environ(Enum):
    DEV = "dev"
    PROD = "prod"


@pytest.fixture(scope="session")
def environ() -> str:
    try:
        return Environ(os.environ["LOOPR_PYTHON_SDK_TEST_ENV"])
    except KeyError:
        raise Exception(f"LOOPR_TEST_ENV VARIABLE MISSING IN {os.environ}")


@pytest.fixture(scope="session")
def testing_url(environ: str) -> str:
    if environ == Environ.PROD:
        return os.environ["LOOPR_PROD_URL"]
    else:
        return os.environ["LOOPR_DEV_URL"]


@pytest.fixture(scope="session")
def testing_api_key(environ: str) -> str:
    if environ == Environ.PROD:
        return os.environ["LOOPR_PROD_API_KEY"]
    else:
        return os.environ["LOOPR_DEV_API_KEY"]


@pytest.fixture(scope="session")
def client(testing_api_key: str, testing_url: str):
    return LooprClient(api_key=testing_api_key, endpoint=testing_url)


@pytest.fixture(scope="class")
def dataset(client: LooprClient):
    name = "test-dataset-" + random_generator()
    dataset = client.create_dataset(
        name=name,
        slug=name,
        type=TEST_IMAGE_DATASET_TYPE,
    )
    yield dataset
    dataset.delete()


@pytest.fixture(scope="class")
def project(client: LooprClient):
    name = "test-project-" + random_generator()
    project = client.create_project(
        name=name,
        slug=name,
        type=TEST_OBJECT_DETECTION_PROJECT_TYPE,
        configuration=TEST_OBJECT_DETECTION_PROJECT_CONFIG,
    )
    yield project
    project.delete()


@pytest.fixture(scope="class")
def dataset_paired(client: LooprClient):
    name = "test-paired-" + random_generator()
    dataset_paired = client.create_dataset(
        name=name,
        slug=name,
        type=TEST_PAIRED_DATASET_TYPE,
        paired_type={"query": "text", "data": "image"},
    )
    yield dataset_paired
    dataset_paired.delete()
