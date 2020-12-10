from loopr.api.dataset.abs_dataset import AbsDataset
from loopr.api.dataset.dataset import Dataset
from loopr.api.row import row_initializer


class SkuDataset(Dataset, AbsDataset):
    @staticmethod
    def _create_dataset_instance(client, **kwargs):
        return SkuDataset(client, kwargs)

    def add_row(self, data: dict, external_id: str = None, **kwargs):
        """
        Add a Single Row in Sku Dataset.

        >>> dataset.add_row(data={
        "sku_id": "A7DVR8JH7WIW",
        "sku_image": "gs://loopr-demo-dataset/a7e9b922-f8d5-43aa-abb9-5a3095f88edc",
        "sku_name": "Digital Innovations EasyGlide Wireless Travel Mouse",
        "sku_url": "gs://loopr-demo-dataset/a7e9b922-f8d5-43aa-abb9-5a3095f88edc",
        "sku_price": "1200",
        "sku_description": "This is a wireless Mouse",
        "sku_brand": "Digital Innovations"})

        :param data: Row Data
        :param external_id: ID provided by user to keep track on row. (Optional)
        :return: A Text Row Instance
        """
        row = row_initializer("sku")
        URL_PATH = "row.sku.create"
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
