from loopr.models.entities.data_types import Field
from loopr.models.entities.loopr_object import LooprObject


class Row(LooprObject):
    entity_type = "row"
    row_id = Field.String("row_id")
    data = Field.String("data")
    successful = Field.String("successful")

    def delete(self, row_ids: list, dataset_id: str):
        URL_PATH = "row.delete"
        request = {"dataset_id": dataset_id, "row_ids": row_ids}
        response = self.client.post(path=URL_PATH, body=request)
        return response
        # logger.info(response)

