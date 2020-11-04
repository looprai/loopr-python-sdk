from loopr.api.dataset.abs_dataset import AbsDataset
from loopr.api.dataset.dataset import Dataset
from loopr.api.row import RowInitializer


class ImageDataset(Dataset, AbsDataset):
    @staticmethod
    def _create_dataset_instance(client, **kwargs):
        return ImageDataset(client, kwargs)

    def add_row(self, **kwargs):
        """
        Add a Single Row in image dataset.

        >>> dataset.add_row(data={"image_url":"gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d"})

        Kwargs:
            data (dict): It contains the row data that is to be added.
            external_id (str): ID provided by user to keep track on row. (Optional)

        Response:
            Returns a Image Row Object.

        """
        row = RowInitializer("image")
        URL_PATH = "row.image.create"
        request = {"dataset_id": self.uid, **kwargs}
        response = self.client.post(path=URL_PATH, body=request)
        return row._add_row_instance(
            self.client, **{**response, "dataset_id": self.uid}
        )
