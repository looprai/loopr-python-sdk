from loopr.api.annotation.annotation import Annotation
from loopr.models.entities.data_types import Field
from loopr.models.entities.loopr_object import LooprObject
from loopr.models.entities.loopr_object_collection import LooprObjectCollection


class Project(LooprObject):
    """
    Projects are a way of organizing similar tasks, so that one can share parameters among tasks.
    A project can attach multiple datasets.
    """

    entity_type = "project"
    project_name = Field.String("project_name")
    project_type = Field.String("project_type")
    project_slug = Field.String("project_slug")
    description = Field.String("description")

    def delete(self):
        """
        Delete the Project.
        >>> project.delete()

        Response :
            :returns "successful" message.
        """
        URL_PATH = "project.delete"
        request = {"project_id": self.uid}
        response = self.client.post(path=URL_PATH, body=request)
        return response["message"]

    def export_configuration(
        self,
    ):
        """
        Export Configuration of Project
        >>> project.export_configuration()

        Response:
            :returns a download url for the project configuration.
        """
        URL_PATH = "project.configuration.export"
        request = {"project_id": self.uid}
        response = self.client.get(path=URL_PATH, params=request)
        return response["download_url"]

    def get_annotations(self, offset: int = 0, **kwargs):
        """
        Gets Annotation data for a project.
        >>> project.get_annotations(offset=0)

        Args:
            offset (int): The no of annotations to skip before fetchng
            start_date (str): The starting range of date.
            end_date (str): The ending range of date.
            external_ids(list): The list of external ids to filter.
            group_ids(list): The list of group ids to filter
            review (list): The list of review flags.
                         allowed flags : - "negative",
                                         - "positive",
                                         - "not_reviewed"
            sort_key(str): The key to sort the result by.
                         Allowed values: - date
            sort_by(str): The order to sort by,
                         Allowed values: - ascending (default)
                                         - descending
        Response:
             :returns a iterable list of Annotations.
        """
        URL_PATH = "project.annotation.list"
        kwargs["project_id"] = self.uid
        return LooprObjectCollection(
            self.client,
            URL_PATH,
            "annotation_data",
            Annotation,
            "POST",
            kwargs,
            offset=offset,
        )
