# Loopr Python SDK
Loopr is a complete Data Labeling Solution for Model Training, Data Augmentation and Quality Control.
Visit https://www.loopr.ai/ for more information.

## Requirements

- Python 3.6+
- Create an account at https://beta-app.loopr.ai/ 
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


## Getting Sarted


#### Creating a Dataset


```python 
dataset =loopr_client.create_dataset(type="<type of dataset>",name="<name for dataset>", slug="<slug for dataset>")
```
- For instance, creating dataset for image type 

  ```python
  dataset = loopr_client.create_dataset(type="image", name="mydataset", slug="mydataset")
  ```

#### Adding Row

 ```python
 dataset.add_row(type="<dataset type>", data="<row data>")
```
- Adding row in image dataset

  ```python
    dataset.add_row(type="image", data={"image_url" : "gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d"})
  ```

#### Deleting Dataset

```python
dataset.delete()
```
- Deleting image dataset

  ```python
    dataset.delete()
  ```
  
#### Deleting Rows

```python
dataset.delete_rows(row_ids = ["list of row ids"])
```

- Deleting image dataset rows 

  ```python
    dataset.delete_rows(["row_id1", "row_id2"])
  ```