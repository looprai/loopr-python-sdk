from loopr.api.row.image_row import ImageRow
from loopr.api.row.paired_row import PairedRow
from loopr.api.row.sku_row import SKURow
from loopr.api.row.text_row import TextRow
from loopr.exceptions import LooprInvalidResourceError
from loopr.resources.constants import INVALID_DATASET


def RowInitializer(dataset_type):
    if not type:
        raise LooprInvalidResourceError(INVALID_DATASET)
    rows = {
        "image": ImageRow,
        "paired": PairedRow,
        "text": TextRow,
        "sku": SKURow,
    }

    return rows[dataset_type]
