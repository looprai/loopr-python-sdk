from loopr.api.dataset.abs_dataset import AbsDataset
from loopr.api.dataset.dataset import Dataset
from loopr.api.row import row_initializer


class TextDataset(Dataset, AbsDataset):
    @staticmethod
    def _create_dataset_instance(client, **kwargs):
        return TextDataset(client, kwargs)

    def add_row(self, data: dict, external_id: str = None, **kwargs):
        """
        Add a Single Row in Text dataset.

        >>> dataset.add_row(data={"text":"This is Sample text row data for Loopr Text Dataset"})


        :param data: Row Data
        :param external_id : ID provided by user to keep track on row. (Optional)
        :return: A Text Row Instance
        """
        row = row_initializer("text")
        URL_PATH = "row.text.create"
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
