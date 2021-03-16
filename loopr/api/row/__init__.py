from loopr.api.row.row import Row


class RowInitializer:
    type = "row"

    @classmethod
    def type_name(cls):
        return cls.type

    def __call__(self):
        return Row


row_initializer = RowInitializer()
