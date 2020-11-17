from loopr.models.entities.data_types import Field
from loopr.models.entities.loopr_object import LooprObject


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
                On successful deletion "successful" will be returned.
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
            Download url for the project will be returned.
        """
        URL_PATH = "project.configuration.export"
        request = {"project_id": self.uid}
        response = self.client.get(path=URL_PATH, params=request)
        return response["download_url"]
