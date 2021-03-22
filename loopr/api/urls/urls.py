class URLS:
    def __init__(self, endpoint):
        self.base_url = endpoint

        # Project
        self.project_create = "project.create"
        self.project_update = "project.update"
        self.project_list = "project.list"
        self.project_info = "project.info"
        self.project_dataset_add = "project.dataset.add"
        self.project_taxonomy_create = "project.taxonomy.create"
        self.project_taxonomy_info = "project.taxonomy.info"
        self.project_taxonomy_update = "project.taxonomy.update"
        self.project_taxonomy_export = "project.taxonomy.export"
        self.project_annotation_list = "project.annotation.list"
        self.project_delete = "project.delete"
        self.project_add_prediction = "project.prediction.add"

        # Dataset
        self.dataset_create = "dataset.create"
        self.dataset_list = "dataset.list"
        self.dataset_info = "dataset.info"
        self.dataset_update = "dataset.update"
        self.dataset_delete = "dataset.delete"
        self.dataset_row_add = "dataset.row.add"
        self.dataset_row_delete = "dataset.row.delete"

    def base_url(self):
        return self.base_url

    def dataset_delete_url(self):
        return self.base_url + self.dataset_delete

    def dataset_info_url(self):
        return self.base_url + self.dataset_info

    def dataset_create_url(self):
        return self.base_url + self.dataset_create

    def dataset_update_url(self):
        return self.base_url + self.dataset_update

    def dataset_row_add_url(self):
        return self.base_url + self.dataset_row_add

    def dataset_row_delete_url(self):
        return self.base_url + self.dataset_row_delete

    def dataset_list_url(self):
        return self.base_url + self.dataset_list

    def project_create_url(self):
        return self.base_url + self.project_create

    def project_update_url(self):
        return self.base_url + self.project_update

    def project_info_url(self):
        return self.base_url + self.project_info

    def project_delete_url(self):
        return self.base_url + self.project_delete

    def project_list_url(self):
        return self.base_url + self.project_list

    def project_dataset_add_url(self):
        return self.base_url + self.project_dataset_add

    def project_taxonomy_create_url(self):
        return self.base_url + self.project_taxonomy_create

    def project_taxonomy_info_url(self):
        return self.base_url + self.project_taxonomy_info

    def project_taxonomy_update_url(self):
        return self.base_url + self.project_taxonomy_update

    def project_taxonomy_export_url(self):
        return self.base_url + self.project_taxonomy_export

    def project_annotation_list_url(self):
        return self.base_url + self.project_annotation_list

    def project_add_prediction_url(self):
        return self.base_url + self.project_add_prediction
