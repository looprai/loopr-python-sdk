from loopr.api.dataset.abs_dataset import AbsDataset
from loopr.api.dataset.dataset import Dataset


class ImageDataset(Dataset, AbsDataset):
    @staticmethod
    def _create_dataset_instance(client,**kwargs):
        return ImageDataset(client,kwargs)