import random
import string

TEST_IMAGE_DATASET_TYPE = "image"
TEST_TEXT_DATASET_TYPE = "text"
TEST_SKU_DATASET_TYPE = "sku"
TEST_OBJECT_DETECTION_PROJECT_TYPE = "object_detection"
TEST_RELEVANCY_PROJECT_TYPE = "relevancy"
TEST_CATEGORIZATION_PROJECT_TYPE = "categorization"
TEST_NER_PROJECT_TYPE = "ner"
TEST_SEGMENTATION_PROJECT_TYPE = "segmentation"
TEST_OCR_PROJECT_TYPE = "ocr"
TEST_INVALID_DATASET_ID = "invaliddatasetid"
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

TEST_CATEGORIZATION_RESPONSE_TAXONOMY = {
    "taxonomy_id": "test_taxonomy_id",
    "labels": None,
    "classifications": [
        {
            "concept_id": "class1",
            "name": "How many shirts ?",
            "required": True,
            "type": "categorical",
            "choices": [
                {"choice_id": "a", "name": "1", "description": None},
                {"choice_id": "b", "name": "2", "description": None},
            ],
            "is_multi": True,
            "condition": None,
        }
    ],
    "instruction": "text instruction",
}


TEST_NER_PROJECT_CONFIG = {
    "taxonomy_id": "tid2",
    "labels": [
        {
            "concept_id": "cid2",
            "name": "noun",
            "color": "#FC7460",
            "type": "bbox",
            "attributes": [
                {
                    "attribute_id": "attr1",
                    "name": "attribute1",
                    "required": True,
                    "is_multi": True,
                    "type": "text",
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
    "instruction": "",
}

TEST_NER_PROJECT_CONFIG_RES = {
    "taxonomy_id": "tid2",
    "labels": [
        {
            "concept_id": "cid2",
            "name": "noun",
            "type": "bbox",
            "color": "#FC7460",
            "attributes": [
                {
                    "attribute_id": "attr1",
                    "name": "attribute1",
                    "required": True,
                    "type": "text",
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
    "instruction": "",
}

TEST_VALID_PREDICTION_BODY = {
    "classifications": [{"concept_id": "class1", "choices": ["a"]}]
}

TEST_NER_PREDICTION_BODY = {
    "labels": [{"concept_id": "cid2", "text": "lorem", "start": 0, "end": 5}]
}

TEST_INVALID_PREDICTION_BODY = {"classifications": [{"choices": ["A", "B"]}]}

TEST_OBJECT_DETECTION_PREDICTION_BODY = {
    "labels": [
        {
            "concept_id": "cid1",
            "coordinates": [
                {"x": 236.33333333333331, "y": 147},
                {"x": 423.3333333333333, "y": 147},
                {"x": 423.3333333333333, "y": 374},
                {"x": 236.33333333333331, "y": 374},
            ],
        }
    ]
}

TEST_SEGMENTATION_PREDICTION_BODY = {
    "labels": [
        {
            "concept_id": "cid1",
            "segment_uri": "https://dev-storage.loopr.ai/loopr-dev-results/d7ea5949-ddc9-4ea6-a711-aac9898dcd46/098ebc86-8edd-4f5d-9e96-603937714ae1/segments/UzKpRFLlt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=RS515W3VYV0U0D2WJRAD%2F20210405%2Feu-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210405T120559Z&X-Amz-Expires=36000&X-Amz-SignedHeaders=host&X-Amz-Signature=83dcf4689f3bf1baacf5fc20bd01affd030fb0a1f3266c89e153948fe8cff609",
        }
    ]
}


def random_generator() -> str:
    letters = string.ascii_lowercase
    random_str = "".join(random.sample(letters, 15))
    return random_str
