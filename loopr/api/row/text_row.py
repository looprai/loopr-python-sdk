from loopr.api.row.abs_row import AbsRow
from loopr.api.row.row import Row


class TextRow(Row, AbsRow):
    """Text Row"""

    @staticmethod
    def _add_row_instance(client, **kwargs):
        return TextRow(client, kwargs)
