================================
Welcome to Loopr's Documentation
================================

Current version is |release|.

Loopr is a complete Data Labeling Solution for Model Training, Data Augmentation and Quality Control.
Visit https://www.loopr.ai/ for more information..

Requirements
============
- Python 3.6+
- Create an account at https://app.loopr.ai/
- Get your API Key from API Keys Tab.

Installation & Authentication
=============================
- Installing package

.. code-block:: bash

   $ pip install loopr

- Set your API Key as an environment variable or you can pass the key while initializing the client.

.. code-block:: bash

   $ export LOOPR_API_KEY = "<your api key>"

or

.. code-block:: python

   from loopr.client import LooprClient
   loopr_client = LooprClient(api_key="<your api key>")


- For enterprise deployments, you can set a custom endpoint as well
  or you can pass the endpoint while initializing the client.

.. code-block:: bash

   $  export LOOPR_API_ENDPOINT = "<your endpoint>"

or

.. code-block:: python

   from loopr.client import LooprClient
   loopr_client = LooprClient(api_key="<your api key>", endpoint="<your endpoint>")

Quickstart
==========

Working with Projects
^^^^^^^^^^^^^^^^^^^^^
Creating a Project
------------------
.. code-block:: python

   from loopr.client import LooprClient
   loopr_client = LooprClient(api_key="<your api key>", endpoint="<your endpoint>")
   project = loopr_client.create_project(
        project_type="object_detection",
        project_name="my-test-project",
        dataset_type="image"
    )
    print(project)

This prints:

.. code-block:: text

    <Project {'project_name': 'my-test-project','project_slug': 'my-test-project', 'uid': '57d4d6d3-cce0-4854-bf4e-8edf9783bba0'}>

Adding Taxonomy/Configuration to Project
----------------------------------------
.. code-block:: python

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
    "instruction": "instruction" })


Exporting project configuration
-------------------------------
.. code-block:: python

    config_download_url =project.export_configuration()

Deleting a Project
------------------
.. code-block:: python

    project.delete()

Working with Datasets
^^^^^^^^^^^^^^^^^^^^^
Creating a Dataset
------------------
.. code-block:: python

   from loopr.client import LooprClient
   loopr_client = LooprClient(api_key="<your api key>", endpoint="<your endpoint>")
   dataset = loopr_client.create_dataset(
        dataset_type="image",
        dataset_name="my-test-dataset",
    )
    print(dataset)

This prints:

.. code-block:: text

   <Dataset {'dataset_name': 'my-test-dataset','dataset_slug': 'my-test-dataset', 'description': '', 'uid': '57d4d6d3-cce0-4854-bf4e-8edf9783bba0'}>

Adding row to Dataset
---------------------
.. code-block:: python

   row = dataset.add_row(data={"image" : "https://loopr.storage/a61a69be-f152-4175-bab4-e119f980bcsd"})

Deleting a row
--------------
.. code-block:: python

   row.delete()

Deleting a dataset
------------------
.. code-block:: python

   dataset.delete()


.. toctree::
   :maxdepth: 2

   Client <client>
   Project <project>
   Dataset <dataset>
   Annotation <annotation>
   Row <row>



