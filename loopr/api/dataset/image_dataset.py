from loopr.api.dataset.abs_dataset import AbsDataset
from loopr.api.dataset.dataset import Dataset
from loopr.api.row import RowInitializer


class ImageDataset(Dataset, AbsDataset):
    @staticmethod
    def _create_dataset_instance(client, **kwargs):
        return ImageDataset(client, kwargs)

    def add_row(self, data, **kwargs):
        row = RowInitializer("image")
        URL_PATH = "row.image.create"
        request = {"dataset_id": self.uid, "data": data, **kwargs}
        response = self.client.post(path=URL_PATH, body=request)
        return row._add_row_instance(
            self.client, **{**response, "dataset_id": self.uid}
        )
