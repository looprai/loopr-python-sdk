import random
import string

TEST_IMAGE_DATASET_TYPE = "image"
TEST_PAIRED_DATASET_TYPE = "paired"
TEST_OBJECT_DETECTION_PROJECT_TYPE = "object_detection"
TEST_RELEVANCY_PROJECT_TYPE = "relevancy"
TEST_OBJECT_DETECTION_PROJECT_CONFIG = {
    "labels": [{"name": "bird", "tool": "bbox", "color": "#000000"}],
    "attributes": [],
}
TEST_RELEVANCY_PROJECT_CONFIG = {
    "question": "string",
    "choices": [{"score": 0, "description": "string"}],
}


def random_generator() -> str:
    letters = string.ascii_lowercase
    random_str = "".join(random.sample(letters, 15))
    return random_str
