from loopr.api.row.abs_row import AbsRow
from loopr.api.row.row import Row


class SkuRow(Row, AbsRow):
    """SKU Row"""

    @staticmethod
    def _add_row_instance(client, **kwargs):
        return SkuRow(client, kwargs)
