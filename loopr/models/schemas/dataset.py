from typing import Optional

from pydantic import BaseModel
from pydantic.json import UUID

class DatasetInCreateRequest(BaseModel):
    name: str
    slug: str
    description: Optional[str]
    paired_type: Optional[dict] = None


class DatasetInCreateResponse(BaseModel):
    dataset_id : UUID
    dataset_slug : str
    dataset_name: str
    description: str

class OperationStatus(BaseModel):
    successful: bool