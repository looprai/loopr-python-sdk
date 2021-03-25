from loopr.api.project.project import Project
from loopr.exceptions import LooprInvalidResourceError
from loopr.resources.constants import (
    INVALID_PROJECT_TYPE,
    categorization_type_project,
    ner_type_project,
    object_detection_type_project,
    ocr_type_project,
    relevancy_type_project,
    segmentation_project,
)


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
                relevancy_type_project: Project,
                object_detection_type_project: Project,
                categorization_type_project: Project,
                ner_type_project: Project,
                ocr_type_project: Project,
                segmentation_project: Project,
            }

            return projects[project_type]
        except KeyError:
            raise LooprInvalidResourceError(INVALID_PROJECT_TYPE)


project_initializer = ProjectInitializer()
