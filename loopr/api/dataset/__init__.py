from loopr.api.dataset.image_dataset import ImageDataset
from loopr.api.dataset.paired_dataset import PairedDataset
from loopr.api.dataset.sku_dataset import SKUDataset
from loopr.api.dataset.text_dataset import TextDataset
from loopr.exceptions import LooprInvalidResourceError
from loopr.resources.constants import INVALID_DATASET


def DatasetInitializer(dataset_type):
    if not type:
        raise LooprInvalidResourceError(INVALID_DATASET)
    datasets = {
        "image": ImageDataset,
        "paired": PairedDataset,
        "text": TextDataset,
        "sku": SKUDataset
    }

    return datasets[dataset_type]
