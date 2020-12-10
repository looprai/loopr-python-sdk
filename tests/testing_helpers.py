import random
import string

TEST_IMAGE_DATASET_TYPE = "image"
TEST_PAIRED_DATASET_TYPE = "paired"
TEST_TEXT_DATASET_TYPE = "text"
TEST_SKU_DATASET_TYPE = "sku"
TEST_OBJECT_DETECTION_PROJECT_TYPE = "object_detection"
TEST_RELEVANCY_PROJECT_TYPE = "relevancy"
TEST_CATEGORIZATION_PROJECT_TYPE = "categorization"
TEST_OBJECT_DETECTION_PROJECT_CONFIG = {
    "labels": [{"name": "bird", "tool": "bbox", "color": "#000000"}],
    "attributes": [],
}
TEST_RELEVANCY_PROJECT_CONFIG = {
    "question": "string",
    "choices": [{"score": 0, "description": "string"}],
}
TEST_CATEGORIZATION_PROJECT_CONFIG = {
    "taxonomies": [
        {
            "name": "question_id",
            "description": "question",
            "type": "categorical",
            "choices": [{"name": "choice", "description": None}],
            "is_multi": True,
        }
    ]
}
PREDICTIONS = [
    {"tool": "point", "coordinates": [{"x": 109.0, "y": 99}]},
    {
        "tool": "bbox",
        "coordinates": {
            "x_top_left": 191,
            "y_top_left": 92,
            "width": 105,
            "height": 92,
        },
    },
    {
        "tool": "line",
        "coordinates": [
            {"x": 279, "y": 263},
            {"x": 555, "y": 211},
        ],
    },
    {
        "tool": "polygon",
        "coordinates": [
            {"x": 161.0, "y": 338.0},
            {"x": 273.0, "y": 311.0},
            {"x": 195.0, "y": 252.0},
        ],
    },
    {
        "tool": "polyline",
        "coordinates": [
            {"x": 511, "y": 355},
            {"x": 418, "y": 460},
            {"x": 649, "y": 373},
            {"x": 519, "y": 356},
            {"x": 573, "y": 291},
        ],
    },
]


def random_generator() -> str:
    letters = string.ascii_lowercase
    random_str = "".join(random.sample(letters, 15))
    return random_str
