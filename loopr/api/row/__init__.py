from loopr.api.row.image_row import ImageRow
from loopr.api.row.paired_row import PairedRow
from loopr.exceptions import LooprInvalidResourceError
from loopr.resources.constants import INVALID_ROW_TYPE


def RowInitializer(dataset_type):
    try:
        rows = {
            "image": ImageRow,
            "paired": PairedRow,
        }

        return rows[dataset_type]
    except KeyError:
        raise LooprInvalidResourceError(INVALID_ROW_TYPE)
