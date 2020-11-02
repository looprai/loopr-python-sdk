from loopr.api.row.abs_row import AbsRow
from loopr.api.row.row import Row


class PairedRow(Row, AbsRow):
    """Paired Row"""

    @staticmethod
    def _add_row_instance(client, **kwargs):
        return PairedRow(client, kwargs)
