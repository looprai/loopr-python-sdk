from loguru import logger

from loopr.api.row import RowInitializer
from loopr.models.entities.data_types import Field
from loopr.models.entities.loopr_object import LooprObject


class Dataset(LooprObject):
    entity_type = "dataset"
    dataset_slug = Field.String("dataset_slug")
    dataset_name = Field.String("dataset_name")
    description = Field.String("description")
    payload_type = Field.String("payload_type")
    projects_attached = Field.Int("projects_attached")
    dataset_rows = Field.Int("projects_attached")

    def delete(self):
        URL_PATH = "dataset.delete"
        request = {"dataset_id": self.uid}
        response = self.client.post(path=URL_PATH, body=request)
        logger.info(response)

    def add_row(self, type: str, **kwargs):
        row = RowInitializer(type)
        URL_PATH = f"row.{type}.create"
        request = {"dataset_id": self.uid, **kwargs}
        response = self.client.post(path=URL_PATH, body=request)
        return row._add_row_instance(self, **response)
