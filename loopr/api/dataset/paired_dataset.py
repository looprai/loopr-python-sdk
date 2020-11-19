from loopr.api.dataset.abs_dataset import AbsDataset
from loopr.api.dataset.dataset import Dataset
from loopr.api.row import row_initializer


class PairedDataset(Dataset, AbsDataset):
    @staticmethod
    def _create_dataset_instance(client, **kwargs):
        return PairedDataset(client, kwargs)

    def add_row(self, data: dict, external_id: str = None, **kwargs):
        """
        Add a Single Row in paired dataset.

        Example of TextImage Paired Dataset :
            >>> dataset.add_row(query={"text":"query"}, data={"image": "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d"})

        Args:
            data (dict): Result Data. Predictions can also be passed in data which is a list of pre-annotated data.
            external_id: (str) ID provided by user to keep track on row. (Optional)

        Kwargs:
            query (dict): Query Data.

        Type of Paired Dataset :
            - TextImage
            - ImageImage
            - TextSKU
            - ImageSKU

        Format of Arguments for different datatypes:
            TextImage : query={"text":"<your query>"}, data={"image":"<image_url>"}
            ImageImage : query={"image":"<your query image>"}, data={"image":"<image_url>"}
            TextSKU : query={"text":"<your query>"}, data={"sku_image":"<image_url>", "sku_name":"<name>"}
            ImageSKU : query={"image":"<your query image>"}, data={"sku_image":"<image_url>", "sku_name":"<name>"}


        Response:
            :returns a Paired Row Object.

        """
        row = row_initializer("paired")
        URL_PATH = "row.paired.create"
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
