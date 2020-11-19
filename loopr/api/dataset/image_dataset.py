from loopr.api.dataset.abs_dataset import AbsDataset
from loopr.api.dataset.dataset import Dataset
from loopr.api.row import row_initializer


class ImageDataset(Dataset, AbsDataset):
    @staticmethod
    def _create_dataset_instance(client, **kwargs):
        return ImageDataset(client, kwargs)

    def add_row(self, data: dict, external_id: str = None, **kwargs):
        """
        Add a Single Row in image dataset.

        >>> dataset.add_row(data={"image_url":"gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d"})

        Args:
            data (dict): Result Data. Predictions can also be passed in data which is a list of pre-annotated data.
            external_id (str): ID provided by user to keep track on row. (Optional)


        Structure for predictions:
            predictions = [{
                                "tool": "point",
                                "coordinates": [{
                                        "x": 109.0,
                                        "y": 99
                                }]
                        },
                        {
                                "tool": "bbox",
                                "coordinates": {
                                        "x_top_left": 191,
                                        "y_top_left": 92,
                                        "width": 105,
                                        "height": 92
                                }
                        },
                        {
                                "tool": "line",
                                "coordinates": [{
                                        "x": 279,
                                        "y": 263
                                }, {
                                        "x": 555,
                                        "y": 211
                                }]
                        },
                        {
                                "tool": "polygon",
                                "coordinates": [{
                                                "x": 161.0,
                                                "y": 338.0
                                        },
                                        {
                                                "x": 273.0,
                                                "y": 311.0
                                        },
                                        {
                                                "x": 195.0,
                                                "y": 252.0
                                        }
                                ]
                        },
                        {
                                "tool": "polyline",
                                "coordinates": [{
                                                "x": 511,
                                                "y": 355
                                        },
                                        {
                                                "x": 418,
                                                "y": 460
                                        },
                                        {
                                                "x": 649,
                                                "y": 373
                                        },
                                        {
                                                "x": 519,
                                                "y": 356
                                        },
                                        {
                                                "x": 573,
                                                "y": 291
                                        }
                                ]
                        }
                ]

        Response:
            :returns a Image Row Object.

        """
        row = row_initializer("image")
        URL_PATH = "row.image.create"
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
