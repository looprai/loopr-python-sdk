import json
from datetime import datetime
from time import sleep

import pytest
import requests

from loopr.api.dataset.dataset import Dataset
from loopr.api.project.project import Project
from loopr.client import LooprClient
from loopr.exceptions import LooprInvalidResourceError
from tests.testing_helpers import (
    TEST_CATEGORIZATION_PROJECT_TYPE,
    TEST_CATEGORIZATION_RESPONSE_TAXONOMY,
    TEST_IMAGE_DATASET_TYPE,
    TEST_INVALID_PREDICTION_BODY,
    TEST_NER_PROJECT_CONFIG,
    TEST_NER_PROJECT_CONFIG_RES,
    TEST_NER_PROJECT_TYPE,
    TEST_OBJECT_DETECTION_PROJECT_CONFIG,
    TEST_OBJECT_DETECTION_PROJECT_CONFIG_RESPONSE,
    TEST_OBJECT_DETECTION_PROJECT_TYPE,
    TEST_OBJECT_DETECTION_UPDATE_PROJECT_CONFIG,
    TEST_OCR_PROJECT_TYPE,
    TEST_RELEVANCY_PROJECT_TYPE,
    TEST_SEGMENTATION_PROJECT_TYPE,
    TEST_SKU_DATASET_TYPE,
    TEST_TAXONOMY_ADD_CATEGORIZATION,
    TEST_TEXT_DATASET_TYPE,
    TEST_VALID_PREDICTION_BODY,
    random_generator,
)


@pytest.mark.usefixtures("project")
class TestProject:
    @pytest.mark.parametrize(
        "test_input",
        [
            (
                {
                    "project_type": TEST_OBJECT_DETECTION_PROJECT_TYPE,
                    "dataset_type": TEST_IMAGE_DATASET_TYPE,
                },
            ),
            (
                {
                    "project_type": TEST_RELEVANCY_PROJECT_TYPE,
                    "dataset_type": TEST_SKU_DATASET_TYPE,
                },
            ),
            (
                {
                    "project_type": TEST_SEGMENTATION_PROJECT_TYPE,
                    "dataset_type": TEST_IMAGE_DATASET_TYPE,
                },
            ),
            (
                {
                    "project_type": TEST_CATEGORIZATION_PROJECT_TYPE,
                    "dataset_type": TEST_TEXT_DATASET_TYPE,
                },
            ),
            (
                {
                    "project_type": TEST_NER_PROJECT_TYPE,
                    "dataset_type": TEST_TEXT_DATASET_TYPE,
                },
            ),
            (
                {
                    "project_type": TEST_OCR_PROJECT_TYPE,
                    "dataset_type": TEST_IMAGE_DATASET_TYPE,
                },
            ),
        ],
    )
    def test_project_creation_deletion(self, client: LooprClient, test_input):
        project_name = "test-project-" + random_generator()
        project = client.create_project(
            project_type=test_input[0]["project_type"],
            project_name=project_name,
            project_slug=project_name,
            dataset_type=test_input[0]["dataset_type"],
        )
        project.delete()
        assert project.uid == project.to_dict()["uid"]
        assert project.project_name == project_name
        with pytest.raises(LooprInvalidResourceError):
            client.create_project(
                project_type="invalid_type",
                project_name=project_name,
                dataset_type=test_input[0]["dataset_type"],
            )
        with pytest.raises(LooprInvalidResourceError):
            project.delete()

    # OBJECT DETECTION TESTS

    def test_taxonomy_add(self, project: Project):
        response = project.add_taxonomy(TEST_OBJECT_DETECTION_PROJECT_CONFIG)
        assert response == "successful"
        with pytest.raises(LooprInvalidResourceError):
            project.add_taxonomy(TEST_INVALID_PREDICTION_BODY)

    def test_get_taxonomy(self, project: Project):
        response = project.get_taxonomy()
        assert response["taxonomy"] == TEST_OBJECT_DETECTION_PROJECT_CONFIG

    def test_export_configuration(self, project: Project):
        download_url = project.export_configuration()
        response = requests.get(download_url)
        assert json.loads(response.text) == {
            "configuration": TEST_OBJECT_DETECTION_PROJECT_CONFIG_RESPONSE
        }

    def test_update_taxonomy(self, project: Project):
        response = project.update_taxonomy(TEST_OBJECT_DETECTION_UPDATE_PROJECT_CONFIG)
        assert response == TEST_OBJECT_DETECTION_UPDATE_PROJECT_CONFIG

    def test_project_listing(self, client: LooprClient, project: Project):
        project_name = []
        projects = client.get_projects()
        for project in projects:
            project_name.append(project.project_name)
        assert project.project_name in project_name

    def test_get_project_info_id(self, client: LooprClient, project: Project):
        response = client.get_project(project_id=project.uid)
        assert response.project_name == project.project_name

    def test_get_project_info_slug(self, client: LooprClient, project: Project):
        response = client.get_project(project_slug=project.project_slug)
        assert response.project_name == project.project_name

    @pytest.mark.parametrize(
        "test_offset, test_filter",
        [
            (0, {}),
            (
                0,
                {
                    "start_date": datetime.now(),
                    "end_date": datetime.now(),
                },
            ),
        ],
    )
    def test_get_annotation(
        self, client: LooprClient, test_offset, test_filter, project: Project
    ):
        annotations = [
            annotation
            for annotation in project.get_annotations(offset=test_offset, **test_filter)
        ]
        assert len(annotations) == 0

    def test_attach_dataset(
        self, client: LooprClient, project: Project, dataset: Dataset
    ):
        response = project.attach_dataset(dataset_ids=[dataset.uid])
        assert response == "successful"

    @pytest.mark.parametrize(
        "test_input",
        [
            ({"project_name": "updatedproject", "description": None},),
            ({"project_name": "updatedproject", "description": "description"},),
            ({"project_name": None, "description": "description"},),
        ],
    )
    def test_update_project(self, project: Project, test_input):
        response = project.update_project(
            project_name=test_input[0]["project_name"],
            description=test_input[0]["description"],
        )
        assert (response["project_name"] == test_input[0]["project_name"]) or (
            response["description"] == test_input[0]["description"]
        )

    # Categorization Tests

    def test_taxonomy_add_catproject(self, project_cat: Project):
        response = project_cat.add_taxonomy(TEST_TAXONOMY_ADD_CATEGORIZATION)
        assert response == "successful"
        with pytest.raises(LooprInvalidResourceError):
            project_cat.add_taxonomy(TEST_INVALID_PREDICTION_BODY)

    def test_taxonomy_get_catproject(self, project_cat: Project):
        response = project_cat.get_taxonomy()
        assert response["taxonomy"] == TEST_CATEGORIZATION_RESPONSE_TAXONOMY

    def test_attach_dataset_cat(
        self, client: LooprClient, project_cat: Project, dataset: Dataset
    ):
        response = project_cat.attach_dataset(dataset_ids=[dataset.uid])
        assert response == "successful"

    def test_add_prediction(
        self, client: LooprClient, project_cat: Project, dataset: Dataset
    ):
        add_row = dataset.add_row(
            data={
                "image": "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d"
            },
        )
        sleep(2)
        response = project_cat.add_predictions(
            experiment_id="newexxperiment",
            row_id=add_row.uid,
            predictions=TEST_VALID_PREDICTION_BODY,
        )
        assert response == "Prediction added successfully"

    # NER Tests

    def test_taxonomy_add_ner(self, project_ner: Project):
        response = project_ner.add_taxonomy(TEST_NER_PROJECT_CONFIG)
        assert response == "successful"
        with pytest.raises(LooprInvalidResourceError):
            project_ner.add_taxonomy(TEST_INVALID_PREDICTION_BODY)

    def test_taxonomy_get_ner(self, project_ner: Project):
        response = project_ner.get_taxonomy()
        assert response["taxonomy"] == TEST_NER_PROJECT_CONFIG_RES

    def test_attach_dataset_ner(
        self, client: LooprClient, project_ner: Project, dataset_text: Dataset
    ):
        response = project_ner.attach_dataset(dataset_ids=[dataset_text.uid])
        assert response == "successful"
