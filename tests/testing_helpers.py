import random
import string

TEST_IMAGE_DATASET_TYPE = "image"
TEST_TEXT_DATASET_TYPE = "text"
TEST_SKU_DATASET_TYPE = "sku"
TEST_OBJECT_DETECTION_PROJECT_TYPE = "object_detection"
TEST_RELEVANCY_PROJECT_TYPE = "relevancy"
TEST_CATEGORIZATION_PROJECT_TYPE = "categorization"
TEST_OBJECT_DETECTION_PROJECT_CONFIG = {
    "taxonomy_id": "tid1",
    "labels": [
        {
            "concept_id": "cid1",
            "name": "string",
            "type": "bbox",
            "color": "#32CD32",
            "attributes": [
                {
                    "attribute_id": "attr1",
                    "name": "attribute1",
                    "required": True,
                    "is_multi": True,
                    "type": "categorical",
                    "choices": [
                        {
                            "choice_id": "cid2",
                            "name": "choice1",
                            "description": "descriptionn",
                        }
                    ],
                },
                {
                    "attribute_id": "attr2",
                    "name": "attribute2",
                    "required": True,
                    "type": "text",
                },
            ],
        }
    ],
    "classifications": [],
    "instruction": "instruction",
}

TEST_TAXONOMY_ADD_CATEGORIZATION = {
    "taxonomy_id": "test_taxonomy_id",
    "classifications": [
        {
            "concept_id": "class1",
            "name": "How many shirts ?",
            "required": True,
            "is_multi": True,
            "choices": [
                {
                    "choice_id": "a",
                    "name": "1",
                },
                {"choice_id": "b", "name": "2"},
            ],
        }
    ],
    "instruction": "text instruction",
}


TEST_OBJECT_DETECTION_UPDATE_PROJECT_CONFIG = {
    "taxonomy_id": "tid1",
    "labels": [
        {
            "concept_id": "cid1",
            "name": "carr",
            "type": "bbox",
            "color": "#32CD32",
            "attributes": [
                {
                    "attribute_id": "attribute1",
                    "name": "attribute1",
                    "required": False,
                    "is_multi": True,
                    "type": "categorical",
                    "choices": [
                        {
                            "choice_id": "cid2",
                            "name": "choice1",
                            "description": "descriptionn",
                        }
                    ],
                },
                {
                    "attribute_id": "attr2",
                    "name": "attribute2",
                    "required": True,
                    "type": "text",
                },
            ],
        }
    ],
    "classifications": [],
    "instruction": "instruction",
}


TEST_OBJECT_DETECTION_PROJECT_CONFIG_RESPONSE = {
    "taxonomy_id": "tid1",
    "labels": [
        {
            "concept_id": "cid1",
            "name": "string",
            "type": "bbox",
            "color": "#32CD32",
            "attributes": [
                {
                    "attribute_id": "attr1",
                    "name": "attribute1",
                    "required": True,
                    "is_multi": True,
                    "type": "categorical",
                    "choices": [
                        {
                            "choice_id": "cid2",
                            "name": "choice1",
                            "description": "descriptionn",
                        }
                    ],
                },
                {
                    "attribute_id": "attr2",
                    "name": "attribute2",
                    "required": True,
                    "type": "text",
                },
            ],
        }
    ],
    "classifications": [],
    "instruction": {"text": "instruction", "type": "md"},
}


TEST_RELEVANCY_PROJECT_CONFIG = {
    "question": "string",
    "choices": [{"score": 0, "description": "string"}],
}
TEST_CATEGORIZATION_PROJECT_CONFIG = {
    "taxonomy_id": "test_taxonomy_id",
    "classifications": [
        {
            "concept_id": "class1",
            "name": "How many shirts ?",
            "required": True,
            "is_multi": True,
            "choices": [
                {
                    "choice_id": "a",
                    "name": "1",
                },
                {"choice_id": "b", "name": "2"},
            ],
        }
    ],
    "instruction": {"text": "text instruction", "type": "md"},
}


TEST_VALID_PREDICTION_BODY = {
    "classifications": [{"concept_id": "class1", "choices": ["a"]}]
}

TEST_INVALID_PREDICTION_BODY = {"classifications": [{"choices": ["A", "B"]}]}


def random_generator() -> str:
    letters = string.ascii_lowercase
    random_str = "".join(random.sample(letters, 15))
    return random_str
