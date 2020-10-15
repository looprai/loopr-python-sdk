from loopr.exceptions import LooprInvalidAttributeError
from loopr.models.entities.data_types import Field


class LooprEntity:
    @classmethod
    def _attributes_of_type(cls, attribute_type):
        for attribute_name in dir(cls):
            attribute = getattr(cls, attribute_name)
            if isinstance(attribute, attribute_type):
                yield attribute

    @classmethod
    def fields(cls):
        for attribute in cls._attributes_of_type(Field):
            yield attribute

    @classmethod
    def field(cls, field_name):
        field_obj = getattr(cls, field_name, None)
        if not isinstance(field_obj, Field):
            raise LooprInvalidAttributeError(cls, field_name)
        return field_obj

    @classmethod
    def type_name(cls):
        return cls.__name__.split(".")[-1]

    @classmethod
    def base_type_name(cls):
        return cls.__base__.__name__.split(".")[-1]
