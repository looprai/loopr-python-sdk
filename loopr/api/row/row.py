from loopr.models.entities.data_types import Field
from loopr.models.entities.loopr_object import LooprObject


class Row(LooprObject):
    """
    Row represents a single entry of data present inside a dataset.
    A dataset is a collection of rows.
    """

    entity_type = "row"
    dataset_id = Field.String("dataset_id")

    def delete(self):
        """
        Delete Row.
        >>> row.delete()

        Response :
            :returns "successful" message.
        """
        URL_PATH = "row.delete"
        request = {"dataset_id": self.dataset_id, "row_ids": [self.uid]}
        response = self.client.post(path=URL_PATH, body=request)
        return response["message"]
