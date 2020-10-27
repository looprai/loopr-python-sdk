from loopr.api.project.object_detection_project import ObjectDetectionProject
from loopr.api.project.relevancy_project import RelevancyProject
from loopr.exceptions import LooprInvalidResourceError
from loopr.resources.constants import INVALID_PROJECT_TYPE


def ProjectInitializer(project_type):
    try:
        projects = {
            "relevancy": RelevancyProject,
            "object_detection": ObjectDetectionProject,
        }

        return projects[project_type]
    except KeyError:
        raise LooprInvalidResourceError(INVALID_PROJECT_TYPE)
