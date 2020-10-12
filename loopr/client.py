import os

from loguru import logger
import requests
from loopr import _LOOPR_API_KEY, DEFAULT_API_ENDPOINT, _LOOPR_API_ENDPOINT
from loopr.api.dataset import DatasetInitializer
from loopr.api.dataset.dataset import Dataset
from loopr.exceptions import LooprAuthenticationError, LooprInternalServerError, LooprInvalidResourceError
from loopr.models.entities.loopr_object_collection import LooprObjectCollection
from loopr.models.schemas.dataset import DatasetInCreateRequest
from loopr.resources.constants import INVALID_LOOPR_KEY
from loopr.utils.response_handler import response_handler
from loopr.utils.retry import retry


class LooprClient:

    def __init__(self,
                 api_key=None,
                 endpoint=DEFAULT_API_ENDPOINT):

        if api_key is None:
            if _LOOPR_API_KEY not in os.environ:
                raise LooprAuthenticationError(
                    INVALID_LOOPR_KEY)
            api_key = os.environ[_LOOPR_API_KEY]
        if _LOOPR_API_ENDPOINT in os.environ:
            endpoint = os.environ[_LOOPR_API_ENDPOINT]
        self.api_key = api_key

        logger.info("Creating Loopr client at '%s'", endpoint)

        self.endpoint = endpoint
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-API-KEY': api_key
        }

    @retry(exception=LooprInternalServerError)
    @response_handler
    def get(self, path: str, params: dict):
        logger.info(self.endpoint + path)
        logger.info(params)
        res = requests.get(url=self.endpoint + path, params=params, headers=self.headers)
        return res

    @retry(exception=LooprInternalServerError)
    @response_handler
    def post(self, path: str, body: dict):
        res = requests.post(url=self.endpoint + path, json=body, headers=self.headers)
        return res

    def create_dataset(self, type: str, name: str, slug: str = None, **kwargs):
        dataset = DatasetInitializer(type)
        URL_PATH = f'dataset.{type}.create'
        request = DatasetInCreateRequest(name=name, slug=slug, **kwargs)
        response = self.post(path=URL_PATH, body=request.dict())
        return dataset._create_dataset_instance(self, **response)

    def get_datasets(self):
        URL_PATH = "dataset.list"
        return LooprObjectCollection(self, URL_PATH, "space_dataset_list", Dataset)

    def create_project(self):
        pass
