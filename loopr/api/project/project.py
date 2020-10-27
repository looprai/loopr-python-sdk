from loopr.models.entities.data_types import Field
from loopr.models.entities.loopr_object import LooprObject


class Project(LooprObject):
    entity_type = "project"
    project_slug = Field.String("project_slug")
    project_name = Field.String("project_name")
    project_type = Field.String("project_type")

    def delete(self):
        URL_PATH = "project.delete"
        request = {"project_id": self.uid}
        response = self.client.post(path=URL_PATH, body=request)
        return response["status"]

    def export_configuration(
        self,
    ):
        URL_PATH = "project.configuration.export"
        request = {"project_id": self.uid}
        response = self.client.get(path=URL_PATH, params=request)
        return response["download_url"]
