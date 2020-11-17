import json

import pytest
import requests

from loopr.api.project.project import Project
from loopr.client import LooprClient
from loopr.exceptions import LooprInvalidResourceError
from tests.testing_helpers import (
    TEST_OBJECT_DETECTION_PROJECT_CONFIG,
    TEST_OBJECT_DETECTION_PROJECT_TYPE,
    TEST_RELEVANCY_PROJECT_CONFIG,
    TEST_RELEVANCY_PROJECT_TYPE,
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
                    "configuration": TEST_OBJECT_DETECTION_PROJECT_CONFIG,
                    "dataset_type": None,
                },
            ),
            (
                {
                    "project_type": TEST_RELEVANCY_PROJECT_TYPE,
                    "configuration": TEST_RELEVANCY_PROJECT_CONFIG,
                    "dataset_type": {
                        "query_datatype": "text",
                        "result_datatype": "image",
                    },
                },
            ),
        ],
    )
    def test_project_creation_deletion(self, client: LooprClient, test_input):
        project_name = "test-project-" + random_generator()
        project = client.create_project(
            type=test_input[0]["project_type"],
            name=project_name,
            slug=project_name,
            configuration=test_input[0]["configuration"],
            dataset_type=test_input[0]["dataset_type"],
        )
        project.delete()
        assert project.project_name == project_name
        with pytest.raises(LooprInvalidResourceError):
            project.delete()

    def test_export_configuration(self, project: Project):
        download_url = project.export_configuration()
        response = requests.get(download_url)
        assert json.loads(response.text) == {
            "configuration": TEST_OBJECT_DETECTION_PROJECT_CONFIG
        }

    def test_project_listing(self, client: LooprClient, project: Project):
        project_name = []
        projects = client.get_projects()
        for project in projects:
            project_name.append(project.project_name)
        assert project.project_name in project_name

    def test_get_project_info_id(self, client: LooprClient, project: Project):
        response = client.get_project_info(project_id=project.uid)
        assert response.project_name == project.project_name

    def test_get_project_info_slug(self, client: LooprClient, project: Project):
        response = client.get_project_info(project_slug=project.project_slug)
        assert response.project_name == project.project_name
