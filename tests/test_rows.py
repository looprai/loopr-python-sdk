from loopr.api.dataset.dataset import Dataset
from loopr.client import LooprClient


class TestRow:
    def test_delete_row_image(self, client: LooprClient, dataset: Dataset):
        row = dataset.add_row(
            data={
                "image": "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d"
            },
        )
        print(row)
        response = row.delete()
        assert response == "successful"
