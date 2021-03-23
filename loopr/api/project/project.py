from loopr.api.annotation.annotation import Annotation
from loopr.api.project.abs_project import AbsProject
from loopr.models.entities.data_types import Field
from loopr.models.entities.loopr_object import LooprObject
from loopr.models.entities.loopr_object_collection import LooprObjectCollection


class Project(LooprObject, AbsProject):
    """
    Projects are a way of organizing similar tasks, so that one can share parameters among tasks.
    A project can attach multiple datasets.
    """

    entity_type = "project"
    project_name = Field.String("project_name")
    project_type = Field.String("project_type")
    project_slug = Field.String("project_slug")
    description = Field.String("description")

    @staticmethod
    def _create_project_instance(client, **kwargs):
        return Project(client, kwargs)

    def delete(self):
        """
        Delete the Project.
        >>> project.delete()

        Response :
            :returns "successful" message.
        """
        URL_PATH = self.client.url_initializer.project_delete_url()
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
        URL_PATH = self.client.url_initializer.project_taxonomy_export_url()
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
        URL_PATH = self.client.url_initializer.project_annotation_list_url()
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

    def attach_dataset(self, dataset_ids: list):
        """
        Attach Dataset to Project.
        >>> project.attach_dataset(dataset_ids=[dataset_id1, ...])

        Args:
            dataset_ids (list): List of dataset ids to be attached.

        Response:
            :returns "successful" message.
        """
        URL_PATH = self.client.url_initializer.project_dataset_add_url()
        request = {"project_id": self.uid, "dataset_ids": dataset_ids}
        response = self.client.post(path=URL_PATH, body=request)
        return response["message"]

    def update_project(self, project_name: str = None, description: str = None):
        """
        Upadte the Project.
        >>> project.update_project(project_name="project_name", description="desc")

        Args:
            dataset_name : Name of dataset.
            description : Dataset description.

        Response:
             :returns project instance.

        """
        URL_PATH = self.client.url_initializer.project_update_url()
        if project_name is None:
            project_name = self.project_name
        if description is None:
            description = self.description
        request = {
            "project_name": project_name,
            "project_id": self.uid,
            "description": description,
        }
        response = self.client.post(path=URL_PATH, body=request)
        return response

    def add_taxonomy(self, taxonomy: dict):
        """
        Add Taxonommy to Project.
        >>> project.add_taxonomy(taxonomy="{dict of taxonomy data}")

        Args:
            taxonomy : Taxonomy/Configuration of project.

        Response:
            :returns successful status
        """
        URL_PATH = self.client.url_initializer.project_taxonomy_create_url()
        request = {"project_id": self.uid, "taxonomy": taxonomy}
        response = self.client.post(path=URL_PATH, body=request)
        return response["message"]

    def update_taxonomy(self, taxonomy: dict):
        """
        Add Taxonommy to Project.
        >>> project.update_taxonomy(taxonomy="{dict of taxonomy data}")

        Args:
            taxonomy : Taxonomy/Configuration of project.

        Response:
            :returns successful status
        """
        URL_PATH = self.client.url_initializer.project_taxonomy_update_url()
        request = {"project_id": self.uid, "taxonomy": taxonomy}
        response = self.client.post(path=URL_PATH, body=request)
        return response["taxonomy"]

    def get_taxonomy(self):
        """
        Returns information of taxonomy of the project.
        >>> project.get_taxonomy()

        Response:
            :returns taxonomy/configuration dictionary.
        """
        URL_PATH = self.client.url_initializer.project_taxonomy_info_url()
        request = {"project_id": self.uid}
        response = self.client.get(path=URL_PATH, params=request)
        return response

    def add_predictions(
        self,
        experiment_id: str,
        predictions: dict,
        row_id: str = None,
        external_id: str = None,
        model_name: str = None,
        model_version: str = None,
    ):
        """
        Add Predictions.
        >>> project.add_predictions(experiment_id="experiment_id", predictions="{dict of prediction data}", row_id="row_id")

        Response:
            :returns successful message
        """
        URL_PATH = self.client.url_initializer.project_add_prediction_url()
        request = {
            "project_id": self.uid,
            "experiment_id": experiment_id,
            ("row_id" if row_id else "external_id"): (
                row_id if row_id else external_id
            ),
            "predictions": predictions,
            "model_name": model_name,
            "model_version": model_version,
        }
        response = self.client.post(path=URL_PATH, body=request)
        return response["message"]
