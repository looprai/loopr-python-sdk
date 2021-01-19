======
Client
======

.. py:class:: LooprClient(api_key=None, endpoint=DEFAULT_API_ENDPOINT)

   Creates a client to access loopr APIs using the API key.

   :param str api_key: The API key for the space that is provided by Loopr.
   :param str endpoint: This parameter can be used to set the API endpoint of enterprise deployment. \
                                      It's an optional parameter.

   :raises LooprAuthenticationError: If API key is not provided.

   |

   .. py:method:: create_dataset(self, dataset_type, dataset_name, dataset_slug, description= ' ', **kwargs)

   Creates a dataset of a given type and name in your team/space.

   :param str dataset_type: The type of dataset you want to create. \
                     Allowed type:\

                        * ``image``\
                        * ``text``
                        * ``sku``

   :param str dataset_name: The name of dataset which is to be created.
   :param str dataset_slug: The slug for dataset which is to be created. It's an optional parameter.
   :param str description: The description of the dataset. It's an optional parameter.
   :return: a Loopr Dataset instance
   :rtype: Dataset

   .. code-block:: python

       from loopr.client import LooprClient
       loopr_client = LooprClient(api_key="<your api key>", endpoint="<your endpoint>")
       image_dataset = client.create_dataset(
            dataset_type="image", dataset_name="image dataset"
        )
        text_dataset = client.create_dataset(
            dataset_type="text",
            dataset_name="text dataset",
        )
        sku_dataset = client.create_dataset(
            dataset_type="sku",
            dataset_name="sku dataset"
        )
        print(image_dataset)
        print(text_dataset)
        print(sku_dataset)

This prints:

   .. code-block:: text

        <ImageDataset {'dataset_name': 'image dataset', 'dataset_slug': 'image-dataset', 'description': '', 'uid': '855c8a8b-3417-4909-8db2-89f4726fbcf6'}>
        <TextDataset {'dataset_name': 'text dataset', 'dataset_slug': 'text-dataset', 'description': '', 'uid': 'cb65bca3-b255-43e9-a8fb-382ab6bf1d8e'}>
        <SkuDataset {'dataset_name': 'sku dataset', 'dataset_slug': 'sku-dataset', 'description': '', 'uid': '50901db4-32e8-481a-840e-262ac912db8c'}>

   |

   .. py:method:: get_dataset(self, dataset_id= None, dataset_slug=None)

    Returns a dataset instance of  particular dataset. Dataset can be fetched with the help of
    ID or slug.

    :param str dataset_id: (optional) The dataset id of the dataset.
    :param str dataset_slug: (optional) The dataset slug of dataset.
    :return: a Loopr Dataset instance
    :rtype: Dataset

    .. code-block:: python

        image_dataset= client.get_dataset(dataset_slug="image-dataset")
        text_dataset= client.get_dataset(dataset_id="cb65bca3-b255-43e9-a8fb-382ab6bf1d8e")
        sku_dataset= client.get_dataset(dataset_id="50901db4-32e8-481a-840e-262ac912db8c")
        print(image_dataset)
        print(text_dataset)
        print(sku_dataset)

   This prints

    .. code-block:: text

        <ImageDataset {'dataset_name': 'image dataset', 'dataset_slug': 'image-dataset', 'description': '', 'uid': '855c8a8b-3417-4909-8db2-89f4726fbcf6'}>
        <TextDataset {'dataset_name': 'text dataset', 'dataset_slug': 'text-dataset', 'description': '', 'uid': 'cb65bca3-b255-43e9-a8fb-382ab6bf1d8e'}>
        <SkuDataset {'dataset_name': 'sku dataset', 'dataset_slug': 'sku-dataset', 'description': '', 'uid': '50901db4-32e8-481a-840e-262ac912db8c'}>

   |

   .. py:method:: get_datasets(self)

   Returns all the datasets in your space/team.

   :return: a Loopr Dataset iterable instance
   :rtype: LooprObjectCollection

   .. code-block:: python

    for dataset in client.get_datasets():
        print(dataset)

   This prints

   .. code-block:: text

        <ImageDataset {'dataset_name': 'image dataset', 'dataset_slug': 'image-dataset', 'description': '', 'uid': '855c8a8b-3417-4909-8db2-89f4726fbcf6'}>
        <TextDataset {'dataset_name': 'text dataset', 'dataset_slug': 'text-dataset', 'description': '', 'uid': 'cb65bca3-b255-43e9-a8fb-382ab6bf1d8e'}>
        <SkuDataset {'dataset_name': 'sku dataset', 'dataset_slug': 'sku-dataset', 'description': '', 'uid': '50901db4-32e8-481a-840e-262ac912db8c'}>

   |

   .. py:method:: create_project(self, project_type, project_name, project_slug, configuration, vote = 1, review = False, **kwargs)

   Creates a project of a given type, name and configuration in your team/space.

   :param str project_type: The type of project you want to create. \
                     Allowed type:

                        * ``object_detection``
                        * ``relevancy``
                        * ``categorization``
   :param str project_name: The name of project which is to be created.
   :param str project_slug: The slug of project which is to be created. It's an optional parameter.
   :param dict configuration: The config dictionary for the project.
   :param int vote: The number of time data has to be annotated. It's optional parameter.
   :param bool review: To turn on review of data after annotation. It's optional parameter.
   :param str description: The description of the project. It's an optional parameter.
   :param dict dataset_type: It's an optional parameter but has to be passed when creating a \
                                ``relevancy`` type project. ex: ``text/image/sku``
   :return: a Loopr project instance
   :rtype: Project

   .. code-block:: python

       from loopr.client import LooprClient
       loopr_client = LooprClient(api_key="<your api key>", endpoint="<your endpoint>")

       object_detection_project = client.create_project(
            project_type="object_detection",
            project_name="object detection project",
            configuration={
                "labels": [{"name": "bird", "tool": "bbox", "color": "#000000"}],
                "attributes": [],
            },
        )

       relevancy_project= client.create_project(
            project_type="relevancy",
            project_name="relevancy project",
            configuration={
                "question": "question",
                "choices": [{"score": 5, "description": "excellent"}],
            },
            dataset_type="text",
        )

       categorization_project= client.create_project(
            project_type="categorization",
            project_name="categorization project",
            configuration={
                "taxonomies": [
                    {
                        "name": "question_id",
                        "description": "question",
                        "type": "categorical",
                        "choices": [{"name": "choice", "description": None}],
                        "is_multi": True,
                    }
                ]
            },
            dataset_type="image",
        )

        print(object_detection_project)
        print(relevancy_project)
        print(categorization_project)

   This prints:

   .. code-block:: text

        <ObjectDetectionProject {'description': None, 'project_name': 'object detection project', 'project_slug': 'object-detection-project', 'project_type': 'object_detection', 'uid': '67a1c405-39af-480e-954c-4e9eb29f14e6'}>
        <RelevancyProject {'description': None, 'project_name': 'relevancy project', 'project_slug': 'relevancy-project', 'project_type': 'search_relevancy', 'uid': 'ac5a0243-4b53-4d8c-a539-4f0dfda86ef8'}>
        <CategorizationProject {'description': None, 'project_name': 'categorization project', 'project_slug': 'categorization-project', 'project_type': 'categorization', 'uid': '30266846-f48f-4a2d-83d1-cca57b93c816'}>

   |

   .. py:method:: get_project(self, project_id= None, project_slug=None)

    Returns a project instance of  particular project. Project can be fetched with the help of
    ID or slug.

    :param str project_id: (optional) The project id of the project.
    :param str project_slug: (optional) The project slug of project.
    :return: a Loopr Project instance
    :rtype: Project

    .. code-block:: python

        object_detection_project= client.get_project(dataset_slug="object-detection-project")
        relevancy_project= client.get_project(project_slug="relevancy-project")
        categorization_project= client.get_project(project_slug="categorization-project")

        print(object_detection_project)
        print(relevancy_project)
        print(categorization_project)

   This prints

    .. code-block:: text

        <ObjectDetectionProject {'description': None, 'project_name': 'object detection project', 'project_slug': 'object-detection-project', 'project_type': 'object_detection', 'uid': '67a1c405-39af-480e-954c-4e9eb29f14e6'}>
        <RelevancyProject {'description': None, 'project_name': 'relevancy project', 'project_slug': 'relevancy-project', 'project_type': 'search_relevancy', 'uid': 'ac5a0243-4b53-4d8c-a539-4f0dfda86ef8'}>
        <CategorizationProject {'description': None, 'project_name': 'categorization project', 'project_slug': 'categorization-project', 'project_type': 'categorization', 'uid': '30266846-f48f-4a2d-83d1-cca57b93c816'}>

   |

   .. py:method:: get_projects(self)

   Returns all the projects in your space/team.

   :return: a Loopr Project iterable instance
   :rtype: LooprObjectCollection

   .. code-block:: python

    for project in client.get_projects():
        print(project)

   This prints

   .. code-block:: text

        <ObjectDetectionProject {'description': None, 'project_name': 'object detection project', 'project_slug': 'object-detection-project', 'project_type': 'object_detection', 'uid': '67a1c405-39af-480e-954c-4e9eb29f14e6'}>
        <RelevancyProject {'description': None, 'project_name': 'relevancy project', 'project_slug': 'relevancy-project', 'project_type': 'search_relevancy', 'uid': 'ac5a0243-4b53-4d8c-a539-4f0dfda86ef8'}>
        <CategorizationProject {'description': None, 'project_name': 'categorization project', 'project_slug': 'categorization-project', 'project_type': 'categorization', 'uid': '30266846-f48f-4a2d-83d1-cca57b93c816'}>
