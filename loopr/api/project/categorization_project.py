from loopr.api.project.abs_project import AbsProject
from loopr.api.project.project import Project


class CategorizationProject(Project, AbsProject):
    """Categorization Project"""

    @staticmethod
    def _create_project_instance(client, **kwargs):
        return CategorizationProject(client, kwargs)
