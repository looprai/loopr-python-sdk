import os
import random
import string
from enum import Enum

import pytest

from loopr.client import LooprClient
from tests.testing_helpers import TEST_IMAGE_DATASET_TYPE


class Environ(Enum):
    DEV = "dev"
    PROD = "prod"


@pytest.fixture
def environ() -> str:
    try:
        return Environ(os.environ["LOOPR_PYTHON_SDK_TEST_ENV"])
    except KeyError:
        raise Exception(f"LOOPR_TEST_ENV VARIABLE MISSING IN {os.environ}")


@pytest.fixture
def testing_url(environ: str) -> str:
    if environ == Environ.PROD:
        return os.environ["LOOPR_PROD_URL"]
    else:
        return os.environ["LOOPR_DEV_URL"]


@pytest.fixture
def testing_api_key(environ: str) -> str:
    if environ == Environ.PROD:
        return os.environ["LOOPR_PROD_API_KEY"]
    else:
        return os.environ["LOOPR_DEV_API_KEY"]


@pytest.fixture
def client(testing_api_key: str, testing_url: str):
    return LooprClient(api_key=testing_api_key, endpoint=testing_url)


@pytest.fixture
def random_generator() -> str:
    letters = string.ascii_lowercase
    random_str = "".join(random.sample(letters, 15))
    return random_str


@pytest.fixture
def dataset(client: LooprClient, random_generator):
    dataset = client.create_dataset(
        name=random_generator,
        slug=random_generator,
        type=TEST_IMAGE_DATASET_TYPE,
    )
    return dataset
