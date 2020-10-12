import abc

class AbsDataset(metaclass=abc.ABCMeta):

    @staticmethod
    @abc.abstractmethod
    def _create_dataset_instance(client,**kwargs):
        pass









