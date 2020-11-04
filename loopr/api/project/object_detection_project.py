from loopr.api.project.abs_project import AbsProject
from loopr.api.project.project import Project


class ObjectDetectionProject(Project, AbsProject):
    """Object Detection Project"""

    @staticmethod
    def _create_project_instance(client, **kwargs):
        return ObjectDetectionProject(client, kwargs)
