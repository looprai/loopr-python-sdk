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

## Getting Sarted




#### Create Project


```python 
project = client.create_project(type="<type of project>",name="<name for project>",slug="<slug for project>", configuration={"labels": ["<list of labels>"], "attributes": ["<list of attributes>"],})
```
- For instance, creating project of type "object_detection"

  ```python
    project = client.create_project(project_type="object_detection",project_name="test-loopr-project",slug="test-looprr-project", configuration={"labels": [{"name": "bird", "tool": "bbox", "color": "#000000"}], "attributes": [],})
  ```
  


#### Project Config Export

```python
config_download_url =project.export_configuration()
```

#### Delete Project

```python
project.delete()
```



#### Create Dataset


```python 
dataset = loopr_client.create_dataset(type="<type of dataset>",name="<name for dataset>", slug="<slug for dataset>")
```
- Creating dataset for image type 

  ```python
  dataset = loopr_client.create_dataset(dataset_type="image", dataset_name="mydataset", dataset_slug="mydataset")
  ```

#### Delete Dataset

```python
dataset.delete()
```
  

#### Add Row

 ```python
 row = dataset.add_row(data="<row data>")
```
- Adding row in image dataset

  ```python
    row = dataset.add_row(data={"image_url" : "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d"})
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
  
  
#### List Datasets

```python
datasets = client.get_datasets()
for dataset in datasets:
    print(dataset)
```
