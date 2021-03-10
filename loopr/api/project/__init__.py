from loopr.api.project.project import Project
from loopr.exceptions import LooprInvalidResourceError
from loopr.resources.constants import INVALID_PROJECT_TYPE


class ProjectInitializer:
    type = "project"

    @classmethod
    def type_name(cls):
        return cls.type

    def __call__(self, project_type):
        """
        Initialize the Project Object with given project_type. (relevancy/object_detection/categorization)
        Args:
            project_type (str): DataType of project.
        Response:
            It will return an instance of project.
        """
        try:
            projects = {
                "relevancy": Project,
                "object_detection": Project,
                "categorization": Project,
                "ner": Project,
            }

            return projects[project_type]
        except KeyError:
            raise LooprInvalidResourceError(INVALID_PROJECT_TYPE)


project_initializer = ProjectInitializer()
