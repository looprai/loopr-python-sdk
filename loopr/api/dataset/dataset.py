from loopr.models.entities.data_types import Field
from loopr.models.entities.loopr_object import LooprObject


class Dataset(LooprObject):
    entity_type = "dataset"
    dataset_name = Field.String("dataset_name")
    description = Field.String("description")

    def delete(self):
        URL_PATH = "dataset.delete"
        request = {"dataset_id": self.uid}
        response = self.client.post(path=URL_PATH, body=request)
        return response["message"]

    def delete_rows(self, row_ids: list):
        URL_PATH = "row.delete"
        request = {"dataset_id": self.uid, "row_ids": row_ids}
        response = self.client.post(path=URL_PATH, body=request)
        return response
