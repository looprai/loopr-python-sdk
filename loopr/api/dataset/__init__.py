from loopr.api.dataset.image_dataset import ImageDataset
from loopr.api.dataset.paired_dataset import PairedDataset
from loopr.exceptions import LooprInvalidResourceError
from loopr.resources.constants import INVALID_DATASET_TYPE


class DatasetInitializer:
    type = "dataset"

    @classmethod
    def type_name(cls):
        return cls.type

    def __call__(self, dataset_type):
        """
        Initialize the Dataset Object with given datatype. (image/paired)

        Args:
            dataset_type (str): DataType of dataset.

        Response:
            It will return an instance of given type of dataset.
        """
        try:
            datasets = {
                "image": ImageDataset,
                "paired": PairedDataset,
            }

            return datasets[dataset_type]
        except KeyError:
            raise LooprInvalidResourceError(INVALID_DATASET_TYPE)


dataset_initializer = DatasetInitializer()
