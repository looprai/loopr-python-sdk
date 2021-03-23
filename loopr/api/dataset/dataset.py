from loopr.api.dataset.abs_dataset import AbsDataset
from loopr.api.row import row_initializer
from loopr.models.entities.data_types import Field
from loopr.models.entities.loopr_object import LooprObject


class Dataset(LooprObject, AbsDataset):
    """
    Dataset is a collection of rows containing data. One Dataset may consists of
    several rows.
    Type of Datasets :
        - Image
        - Text
        - SKU
    """

    entity_type = "dataset"
    dataset_name = Field.String("dataset_name")
    dataset_slug = Field.String("dataset_slug")
    dataset_type = Field.String("dataset_type")
    description = Field.String("description")

    @staticmethod
    def _create_dataset_instance(client, **kwargs):
        return Dataset(client, kwargs)

    def delete(self):
        """
        Delete the Dataset.
        >>> dataset.delete()

        Response :
            :returns "successful" message.
        """

        URL_PATH = self.client.url_initializer.dataset_delete_url()
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

        URL_PATH = self.client.url_initializer.dataset_row_delete_url()
        request = {"dataset_id": self.uid, "row_ids": row_ids}
        response = self.client.post(path=URL_PATH, body=request)
        return response["message"]

    def add_row(self, data: dict, external_id: str = None, **kwargs):
        """
        Add a Single Row in Dataset.

        For Image :
            >>> dataset.add_row(data={"image":"gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d"})
        For Text :
            >>> dataset.add_row(data={"text":"someText"})
        For SKU :
            >>> dataset.add_row(data={"sku_id": "A7DVR8JH7WIW",
                        "sku_image": "gs://loopr-demo-dataset/a7e9b922-f8d5-43aa-abb9-5a3095f88edc",
                        "sku_name": "Digital Innovations EasyGlide Wireless Travel Mouse",
                        "sku_url": "gs://loopr-demo-dataset/a7e9b922-f8d5-43aa-abb9-5a3095f88edc",
                        "sku_price": "1200",
                        "sku_description": "This is a wireless Mouse",
                        "sku_brand": "Digital Innovations"})

        Args:
            data : Row Data
            external_id : ID provided by user to keep track on row. (Optional)

        Response:
            :return a Row Instance
        """
        row = row_initializer()
        URL_PATH = self.client.url_initializer.dataset_row_add_url()
        request = {
            "dataset_id": self.uid,
            "data": data,
            "external_id": external_id,
            **kwargs,
        }
        response = self.client.post(path=URL_PATH, body=request)
        return row._add_row_instance(
            self.client, **{**response, "dataset_id": self.uid}
        )

    def update_dataset(self, dataset_name: str = None, description: str = None):
        """
        Upadte the Dataset.
        >>> dataset.update_dataset(dataset_name="dataset.name", description="desc")

        Args:
            dataset_name : Name of dataset.
            description : Dataset description.

        Response:
             :returns dataset instance.

        """
        URL_PATH = self.client.url_initializer.dataset_update_url()
        if dataset_name is None:
            dataset_name = self.dataset_name
        if description is None:
            description = self.description
        request = {
            "dataset_name": dataset_name,
            "dataset_id": self.uid,
            "description": description,
        }
        response = self.client.post(path=URL_PATH, body=request)
        return response
