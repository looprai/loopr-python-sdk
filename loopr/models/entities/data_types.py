from enum import Enum, auto


class Field:
    class Type(Enum):
        Int = auto()
        Float = auto()
        String = auto()
        Boolean = auto()
        DateTime = auto()

    @staticmethod
    def Int(*args):
        return Field(Field.Type.Int, *args)

    @staticmethod
    def Float(*args):
        return Field(Field.Type.Float, *args)

    @staticmethod
    def String(*args):
        return Field(Field.Type.String, *args)

    @staticmethod
    def Boolean(*args):
        return Field(Field.Type.Boolean, *args)

    @staticmethod
    def DateTime(*args):
        return Field(Field.Type.DateTime, *args)

    def __init__(self, field_type: Type, name):
        self.field_type = field_type
        self.name = name
