import abc


class AbsProject(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def _create_project_instance(client, **kwargs):
        pass
