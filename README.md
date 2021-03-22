# Loopr Python SDK
Loopr is a complete Data Labeling Solution for Model Training, Data Augmentation and Quality Control.
Visit https://www.loopr.ai/ for more information.

## Requirements

- Python 3.6+
- Create an account at https://app.loopr.ai/ 
- Get your API Key from API Keys Tab.


## Installation & Authentication

Prerequisite : pip
1. Install loopr using `pip install loopr`
2. Set your API Key as an environment variable.

    ```
    export LOOPR_API_KEY = "<your api key>"
    ```
    
    or
   
   you can pass the key while initializing the client.
   
   ```python
   loopr_client = LooprClient(api_key="<your api key>")
   ```
3. You can set a custom endpoint as well.

   ```
    export LOOPR_API_ENDPOINT = "<your endpoint>"
   ```
   
   or
   
   you can pass the endpoint while initializing the client.
   
   ```python
    loopr_client = LooprClient(api_key="<your api key>", endpoint="<your endpoint>")
   ```

## Getting Started


## Project

#### Create Project


```python 
project = client.create_project(project_type="<type of project>",project_name="<name for project>",project_slug="<slug for project>", dataset_type="<dataset type for project>")
```
- For instance, creating project of type "object_detection"

  ```python
    project = client.create_project(project_type="object_detection",project_name="test-loopr-project",slug="test-looprr-project", dataset_type="image")
  ```
  
#### Add Taxonomy
```python
project.add_taxonomy(taxonomy="<taxonomy/configuration of project>")
```
- For instance, adding taxonomy for project type "object_detection"

  ```python
    project.add_taxonomy(taxonomy={
    "taxonomy_id": "tid1",
    "labels": [
        {
            "concept_id": "cid1",
            "name": "string",
            "type": "bbox",
            "color": "#32CD32",
            "attributes": [
                {
                    "attribute_id": "attr1",
                    "name": "attribute1",
                    "required": True,
                    "is_multi": True,
                    "type": "categorical",
                    "choices": [
                        {
                            "choice_id": "cid2",
                            "name": "choice1",
                            "description": "descriptionn",
                        }
                    ],
                },
                {
                    "attribute_id": "attr2",
                    "name": "attribute2",
                    "required": True,
                    "type": "text",
                },
            ],
        }
    ],
    "classifications": [],
    "instruction": "instruction"
  })
  ```


#### Update Project
```python
project.update_project(project_name = "<updated project name>", description = "<updated description>")
```

#### Update Taxonomy
```python
project.update_taxonomy(taxonomy="<updated taxonomy>")
```

#### Attach Dataset
```python
project.attach_dataset(dataset_ids="<list of dataset ids to be attached>")
```

#### Project Config Export

```python
config_download_url = project.export_configuration()
```

#### Get Project
User can fetch a project by either passing the *project id* or *project slug*.
```python
project = client.get_project(project_id = "<id of project>")
```
or
```python
project = client.get_project(project_slug = "<slug for project>")
```

#### Get Taxonomy/Configuration
```python
project.get_taxonomy()
```

#### Delete Project

```python
project.delete()
```

#### Add Predictions
```python
project.add_predictions(experiment_id="<experiment_id>", row_id="<row_id>", predictions="<prediction data>")
```

#### List Projects

```python
projects = client.get_projects()
for project in projects:
    print(project)
```


## Dataset

#### Create Dataset


```python 
dataset = loopr_client.create_dataset(dataset_type="<type of dataset>",dataset_name="<name for dataset>", dataset_slug="<slug for dataset>")
```
- Creating dataset for image type 

  ```python
  dataset = loopr_client.create_dataset(dataset_type="image", dataset_name="mydataset", dataset_slug="mydataset")
  ```

#### Update Dataset
```python
dataset.update_dataset(dataset_name = "<updated dataset name>", description = "<updated description>")
```

#### Get Dataset
User can fetch a dataset by either passing the *dataset id* or *dataset slug*.
```python
dataset = client.get_dataset(dataset_id = "<id of dataset>")
```
or
```python
dataset = client.get_dataset(dataset_slug = "<slug for dataset>")
```

#### Delete Dataset

```python
dataset.delete()
```

#### List Datasets

```python
datasets = client.get_datasets()
for dataset in datasets:
    print(dataset)
```


## Row

#### Add Row

 ```python
 row = dataset.add_row(data="<row data>")
```
- Adding row in image dataset

  ```python
    row = dataset.add_row(data={"image_url" : "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d"})
  ```
- Adding row in image dataset with query (only valid for relevancy project)
  ```python
    row = dataset.add_row(data={"image_url" : "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d", "query":"myquery"})
  ```


#### Delete Row

 ```python
 row.delete()
```


#### Bulk Row Delete

```python
dataset.delete_rows(row_ids = ["list of row ids"])
```

- Deleting image dataset rows 

  ```python
    dataset.delete_rows(["row_id1", "row_id2"])
  ```
  
  
