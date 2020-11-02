from loopr.api.project.abs_project import AbsProject
from loopr.api.project.project import Project


class RelevancyProject(Project, AbsProject):
    """Relevancy Project"""

    @staticmethod
    def _create_project_instance(client, **kwargs):
        return RelevancyProject(client, kwargs)
