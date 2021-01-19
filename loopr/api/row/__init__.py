from loopr.api.row.image_row import ImageRow
from loopr.api.row.sku_row import SkuRow
from loopr.api.row.text_row import TextRow
from loopr.exceptions import LooprInvalidResourceError
from loopr.resources.constants import INVALID_ROW_TYPE


class RowInitializer:
    type = "row"

    @classmethod
    def type_name(cls):
        return cls.type

    def __call__(self, dataset_type):
        """
        Initialize the Row Object with given dataset_type.

        Args:
            dataset_type (str): DataType of dataset. (image/text/sku)

        Response:
            It will return an instance of row of given type.
        """
        try:
            rows = {
                "image": ImageRow,
                "text": TextRow,
                "sku": SkuRow,
            }

            return rows[dataset_type]
        except KeyError:
            raise LooprInvalidResourceError(INVALID_ROW_TYPE)


row_initializer = RowInitializer()
