from loopr.api.row.abs_row import AbsRow
from loopr.models.entities.data_types import Field
from loopr.models.entities.loopr_object import LooprObject


class Row(LooprObject, AbsRow):
    """
    Row represents a single entry of data present inside a dataset.
    A dataset is a collection of rows.
    """

    entity_type = "row"
    dataset_id = Field.String("dataset_id")

    @staticmethod
    def _add_row_instance(client, **kwargs):
        return Row(client, kwargs)

    def delete(self):
        """
        Delete Row.
        >>> row.delete()

        Response :
            :returns "successful" message.
        """
        URL_PATH = self.client.url_initializer.dataset_row_delete_url()
        request = {"dataset_id": self.dataset_id, "row_ids": [self.uid]}
        response = self.client.post(path=URL_PATH, body=request)
        return response["message"]
