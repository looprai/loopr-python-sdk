import os

import requests
from loguru import logger

from loopr import _LOOPR_API_ENDPOINT, _LOOPR_API_KEY, DEFAULT_API_ENDPOINT
from loopr.api.dataset import DatasetInitializer
from loopr.api.dataset.dataset import Dataset
from loopr.api.project import ProjectInitializer
from loopr.exceptions import LooprAuthenticationError, LooprInternalServerError
from loopr.models.entities.loopr_object_collection import LooprObjectCollection
from loopr.resources.constants import INVALID_LOOPR_KEY
from loopr.utils.response_handler import response_handler
from loopr.utils.retry import retry


class LooprClient:
    def __init__(self, api_key=None, endpoint=DEFAULT_API_ENDPOINT):

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
        self, type: str, name: str, slug: str, description: str = "", **kwargs
    ):
        dataset = DatasetInitializer(type)
        URL_PATH = f"dataset.{type}.create"
        response = self.post(
            path=URL_PATH,
            body={"name": name, "slug": slug, "description": description, **kwargs},
        )
        return dataset._create_dataset_instance(self, **response)

    def get_datasets(self):
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
