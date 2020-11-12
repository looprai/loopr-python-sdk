from loopr.api.project.categorization_project import CategorizationProject
from loopr.api.project.object_detection_project import ObjectDetectionProject
from loopr.api.project.relevancy_project import RelevancyProject
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
            It will return an instance of project of given type.
        """
        try:
            projects = {
                "relevancy": RelevancyProject,
                "object_detection": ObjectDetectionProject,
                "categorization": CategorizationProject,
            }

            return projects[project_type]
        except KeyError:
            raise LooprInvalidResourceError(INVALID_PROJECT_TYPE)


project_initializer = ProjectInitializer()
