from loopr.api.dataset.abs_dataset import AbsDataset
from loopr.api.dataset.dataset import Dataset
from loopr.models.schemas.dataset import DatasetInCreateRequest, DatasetInCreateResponse


class TextDataset(Dataset,AbsDataset):
    pass