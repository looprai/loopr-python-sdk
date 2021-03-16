from loopr.api.dataset.dataset import Dataset
from loopr.exceptions import LooprInvalidResourceError
from loopr.resources.constants import (
    INVALID_DATASET_TYPE,
    image_type_dataset,
    sku_type_dataset,
    text_type_dataset,
)


class DatasetInitializer:
    type = "dataset"

    @classmethod
    def type_name(cls):
        return cls.type

    def __call__(self, dataset_type):
        """
        Initialize the Dataset Object with given datatype. (image/text/sku)
        Args:
            dataset_type (str): DataType of dataset.
        Response:
            It will return an instance of dataset.
        """
        try:
            datasets = {
                image_type_dataset: Dataset,
                text_type_dataset: Dataset,
                sku_type_dataset: Dataset,
            }

            return datasets[dataset_type]
        except KeyError:
            raise LooprInvalidResourceError(INVALID_DATASET_TYPE)


dataset_initializer = DatasetInitializer()
