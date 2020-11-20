import abc


class AbsDataset(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def _create_dataset_instance(client, **kwargs):
        pass

    @abc.abstractmethod
    def add_row(self, client, data, external_id, **kwargs):
        pass
