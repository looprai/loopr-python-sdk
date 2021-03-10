import json
from datetime import datetime

import pytest
import requests

from loopr.api.dataset.dataset import Dataset
from loopr.api.project.project import Project
from loopr.client import LooprClient
from loopr.exceptions import LooprInvalidResourceError
from tests.testing_helpers import (
    TEST_CATEGORIZATION_PROJECT_TYPE,
    TEST_IMAGE_DATASET_TYPE,
    TEST_OBJECT_DETECTION_PROJECT_CONFIG,
    TEST_OBJECT_DETECTION_PROJECT_CONFIG_RESPONSE,
    TEST_OBJECT_DETECTION_PROJECT_TYPE,
    TEST_OBJECT_DETECTION_UPDATE_PROJECT_CONFIG,
    TEST_RELEVANCY_PROJECT_TYPE,
    TEST_SKU_DATASET_TYPE,
    TEST_TEXT_DATASET_TYPE,
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
                    "project_type": TEST_CATEGORIZATION_PROJECT_TYPE,
                    "dataset_type": TEST_TEXT_DATASET_TYPE,
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

    def test_taxonomy_add(self, project: Project):
        response = project.add_taxonomy(TEST_OBJECT_DETECTION_PROJECT_CONFIG)
        assert response == "successful"

    def test_get_taxonomy(self, project: Project):
        response = project.get_taxonomy()
        assert response["taxonomy"] == TEST_OBJECT_DETECTION_PROJECT_CONFIG

    def test_export_configuration(self, project: Project):
        download_url = project.export_configuration()
        response = requests.get(download_url)
        print(response.text)
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

    def test_update_project(self, project: Project):
        response = project.update_project(project_name="newprojectname")
        assert response["project_name"] == "newprojectname"
