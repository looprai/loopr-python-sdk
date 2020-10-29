from loopr.models.entities.data_types import Field
from loopr.models.entities.loopr_object import LooprObject


class Row(LooprObject):
    entity_type = "row"
    dataset_id = Field.String("dataset_id")

    def delete(self):
        URL_PATH = "row.delete"
        request = {"dataset_id": self.dataset_id, "row_ids": [self.uid]}
        response = self.client.post(path=URL_PATH, body=request)
        return response["message"]
