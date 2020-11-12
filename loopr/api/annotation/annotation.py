from loopr.models.entities.data_types import Field
from loopr.models.entities.loopr_object import LooprObject


class Annotation(LooprObject):
    entity_type = "job"
    submitted_at = Field.DateTime("submitted_at")
    annotation_data = Field.Dict("annotation_data")
    row = Field.Dict("row")
