import os

import requests
from loguru import logger

from loopr import _LOOPR_API_ENDPOINT, _LOOPR_API_KEY, DEFAULT_API_ENDPOINT
from loopr.api.dataset import DatasetInitializer
from loopr.api.dataset.dataset import Dataset
from loopr.api.project import ProjectInitializer
from loopr.api.project.project import Project
from loopr.exceptions import LooprAuthenticationError, LooprInternalServerError
from loopr.models.entities.loopr_object_collection import LooprObjectCollection
from loopr.resources.constants import INVALID_LOOPR_KEY
from loopr.utils.common_utils import slug_create
from loopr.utils.response_handler import response_handler
from loopr.utils.retry import retry


class LooprClient:
    """
    This is the Loopr Client. This Client is used to initialize API key and Endpoint
    which are necessary to connect to the Loopr Server.
    """

    def __init__(self, api_key=None, endpoint=DEFAULT_API_ENDPOINT):
        """
        Creates and Initialize Loopr Client.
        >>> client = LooprClient(api_key="<api_key>")
        Args:
            api_key (str): API_KEY can provided at the time of initializing the client.
                If None, environment variable "LOOPR_API_KEY" will be used.

            endpoint (str): Default API Endpoint of Loopr Server.
        """
        if api_key is None:
            if _LOOPR_API_KEY not in os.environ:
                raise LooprAuthenticationError(INVALID_LOOPR_KEY)
            api_key = os.environ[_LOOPR_API_KEY]
        if _LOOPR_API_ENDPOINT in os.environ:
            endpoint = os.environ[_LOOPR_API_ENDPOINT]
        self.api_key = api_key

        logger.info(f"Creating Loopr client at {endpoint}")

        self.endpoint = endpoint
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-API-KEY": api_key,
        }

    @retry(exception=LooprInternalServerError)
    @response_handler
    def get(self, path: str, params: dict):
        logger.info(self.endpoint + path)
        logger.info(params)
        res = requests.get(
            url=self.endpoint + path, params=params, headers=self.headers
        )
        return res

    @retry(exception=LooprInternalServerError)
    @response_handler
    def post(self, path: str, body: dict):
        res = requests.post(url=self.endpoint + path, json=body, headers=self.headers)
        return res

    def create_dataset(
        self, type: str, name: str, slug: str = None, description: str = "", **kwargs
    ):
        """
        Create a Dataset of given name and type.
        >>> dataset = client.create_dataset(type="image",name="loopr-test-dataset",slug="loopr-test-slug")

        Args:
            type (str): Type of Dataset (image/paired).
            name (str): Name of Dataset.
            slug (str): Slug of Dataset.
            description (str): Description for Dataset. (Optional)

        Response:
            On successful creation it return a Dataset Object.
        """
        dataset = DatasetInitializer(type)
        URL_PATH = f"dataset.{type}.create"
        if slug is None:
            slug = slug_create(name)
        response = self.post(
            path=URL_PATH,
            body={"name": name, "slug": slug, "description": description, **kwargs},
        )
        return dataset._create_dataset_instance(self, **response)

    def get_datasets(self):
        """
        List all Datasets.
        >>> client.get_datasets()

        Response:
            Returns all datasets.
        """
        URL_PATH = "dataset.list"
        return LooprObjectCollection(self, URL_PATH, "space_dataset_list", Dataset)

    def create_project(
        self,
        type: str,
        name: str,
        slug: str,
        configuration: dict,
        vote: int = 1,
        review: bool = False,
        **kwargs,
    ):
        """
        Create Project.
        >>> client.create_project(type="object_detection",name="test-loopr-project",slug="test-looprr-project",
        >>>                       configuration={"labels": [{"name": "bird", "tool": "bbox", "color": "#000000"}],"attributes": [],})

        Args:
            type (str): Type of Project. (object_detection/relevancy)
            name (str): Name of Project.
            slug (str): Slug of Project.
            review (bool): Either reviews are allowed or not. By default review = false. (true/false)
            vote (int): Number of times a data can be annotated by different annotators.
            configuration (dict): Configuration consists of information regarding the tools used for annotation.

                Configuration consists of following :
                    - labels : It consists of label_name, type of tool and color.
                    - attributes : It consists of properties that are attached to different labels.

                Type of tools :
                    - Point
                    - Bounding Box
                    - Line
                    - Polygon
                    - Polyline

                Color :
                    Here color describes the color of the selected tool. It can be in hex(#FF0000) or rgb(rgb(255, 0, 0)) format.

                For instance :
                    {"configuration": {"labels": [{"name": "car", "tool": "bbox", "color": "#FC7460"}], "attributes": [{"name": "Visibility", "description": "", "conditions": {"label_conditions": {"labels": ["car"]}},
                                                                                                        "required": true, "type": "categorical", "choices": ["Full View", "Partial View"], "is_multi": false},]}}


        Response:
            On successful creation it returns a Project Object.
        """
        project = ProjectInitializer(type)
        URL_PATH = f"project.{type.replace('_','.')}.create"
        response = self.post(
            path=URL_PATH,
            body={
                "project_name": name,
                "slug": slug,
                "configuration": configuration,
                "vote": vote,
                "review": review,
                **kwargs,
            },
        )
        return project._create_project_instance(self, **response)

    def get_projects(self):
        """
        List all Projects.
        >>> client.get_projects()

        Response:
            Returns all projects.
        """
        URL_PATH = "project.list"
        return LooprObjectCollection(self, URL_PATH, "projects_list", Project)

    def get_project_info(self, project_id: str = None, project_slug: str = None):
        URL_PATH = "project.info"
        request = (
            {"project_id": project_id} if project_id else {"project_slug": project_slug}
        )
        response = self.get(
            path=URL_PATH,
            params=request,
        )
        project = ProjectInitializer(response["project_type"])
        return project._create_project_instance(self, **response)

    def get_dataset_info(self, dataset_id: str = None, dataset_slug: str = None):
        URL_PATH = "dataset.info"
        request = (
            {"dataset_id": dataset_id} if dataset_id else {"dataset_slug": dataset_slug}
        )
        response = self.get(
            path=URL_PATH,
            params=request,
        )
        dataset = DatasetInitializer(response["dataset_type"])
        return dataset._create_dataset_instance(self, **response)
