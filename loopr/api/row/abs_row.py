import abc


class AbsRow(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def _add_row_instance(client, **kwargs):
        pass
