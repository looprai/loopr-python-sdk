from loopr.models.entities.data_types import Field
from loopr.models.entities.loopr_object import LooprObject


class Dataset(LooprObject):
    """
    Dataset is a collection of rows containing data. One Dataset may consists of
    several rows.
    Type of Datasets :
        - Image
        - Text
        - SKU
        - Paired (TextImage/ImageImage/TextSKU/ImageSKU)
    """

    entity_type = "dataset"
    dataset_name = Field.String("dataset_name")
    dataset_slug = Field.String("dataset_slug")
    description = Field.String("description")

    def delete(self):
        """
        Delete the Dataset.
        >>> dataset.delete()

        Response :
            :returns "successful" message.
        """

        URL_PATH = "dataset.delete"
        request = {"dataset_id": self.uid}
        response = self.client.post(path=URL_PATH, body=request)
        return response["message"]

    def delete_rows(self, row_ids: list):
        """
        Delete multiple rows present inside dataset.
        >>> dataset.delete_rows([row_id1, row_id2])

        Args:
            row_ids : A list of row ids to be deleted.

        Response :
            :returns "successful" message.

        """

        URL_PATH = "row.delete"
        request = {"dataset_id": self.uid, "row_ids": row_ids}
        response = self.client.post(path=URL_PATH, body=request)
        return response["message"]
