from loopr.api.row.abs_row import AbsRow
from loopr.api.row.row import Row


class ImageRow(Row, AbsRow):
    """Image Row"""

    @staticmethod
    def _add_row_instance(client, **kwargs):
        return ImageRow(client, kwargs)
