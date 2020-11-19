from datetime import timezone

from dateutil.parser import parse
from loguru import logger

from loopr.models.entities.data_types import Field
from loopr.models.entities.loopr_enitity import LooprEntity


class LooprObject(LooprEntity):
    uid = Field.String("uid")

    def __init__(self, client=None, field_values=None):
        if field_values and client:
            self.client = client
            self._set_field_values(field_values)

    def _set_field_values(self, field_values):
        for field in self.fields():
            try:
                if field.name == "uid":
                    value = field_values[self._get_unique_id()]
                else:
                    value = field_values[field.name]
            except KeyError as key_error:
                value = None
                logger.debug(key_error)
            if field.field_type == Field.Type.DateTime and value is not None:
                try:
                    value = parse(value)
                    value = value.replace(tzinfo=timezone.utc)
                except ValueError:
                    logger.warning(
                        f"Failed to convert value {value} to datetime for "
                        f"field {field}"
                    )
            setattr(self, field.name, value)

    def _get_unique_id(
        self,
    ):
        return self.entity_type + "_id"

    def __repr__(self):
        type_name = self.type_name()
        if "uid" in self.__dict__:
            return "<%s ID: %s>" % (type_name, self.uid)
        else:
            return "<%s>" % type_name

    def __str__(self):
        attribute_values = {
            field.name: getattr(self, field.name) for field in self.fields()
        }
        return "<%s %s>" % (self.type_name().split(".")[-1], attribute_values)

    def __eq__(self, other):
        return self.type_name() == other.type_name() and self.uid == other.uid

    def __hash__(self):
        return 7541 * hash(self.type_name()) + hash(self.uid)

    def to_dict(self):
        object_dict = self.__dict__.copy()
        del object_dict["client"]
        return object_dict
