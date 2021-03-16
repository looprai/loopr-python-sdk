=======
Dataset
=======

.. py:class:: Dataset()

    Dataset is a collection of rows containing data. One Dataset may consists of several rows.
        Type of Datasets :
            - image
            - sku
            - text

   .. py:attribute:: uid
    :type: uuid

   |

   .. py:attribute:: dataset_name
    :type: str

   |

   .. py:attribute:: dataset_slug
    :type: str

   |

   .. py:attribute:: description
    :type: str

   |

   .. py:method:: add_row(self, data: dict, external_id: str = None, **kwargs)

    Adds rows to dataset

    :param dict data: Row data to create rows.Format of Arguments for different datatypes:

                * image:
                    ``data={"image":"< image_url >"}``
                * text:
                    ``data={"text":"<your text>"}``
                * sku:
                    ``data={"sku_image":"< image_url >", "sku_name":"<your sku name>"}``
                Prediction is an optional field that can be passed with the data dict. The format of prediction depends \
                on different type of project.

                * object_detection:
                    ``[{"tool": "point", "coordinates": [{"x": 100, "y": 100}]}]``
                * relevancy:
                    ``[{"taxonomy_name":"relevancy","value":["1"]}]``
                Query is an optional string field that can be passed with data dict. It is only valid for image and sku dataset type.

                * image:
                    ``data={"image":"< image_url >", "query":"<your query>"}``
                * sku:
                    ``data={"sku_image":"< image_url >", "sku_name":"<your sku name>", "query":"<your query>"}``

    :param str external_id: (Optional) An unique field that a user can provide to represent rows.

    :return: returns a Row instance
    :rtype: Row

    .. code-block:: python

        image_dataset = client.get_dataset(dataset_id="<dataset_id>")
        image_row= image_dataset.add_row(data={"image":"gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d"})
        text_dataset = client.get_dataset(dataset_id="<dataset_id>")
        text_row = text_dataset.add_row(data={"text":"text data"})
        sku_dataset = client.get_dataset(dataset_id="<dataset_id>")
        sku_row = sku_dataset.add_row(data={"sku_image": "gs://loopr-demo-dataset/a7e9b922-f8d5-43aa-abb9-5a3095f88edc","sku_name": "product name"})

        print(image_row)
        print(text_row)
        print(sku_row)

    This prints

    .. code-block:: text

        <Row {'dataset_id': '< dataset id >', 'uid': '< row id >'}>
        <Row {'dataset_id': '< dataset id >', 'uid': '< row_id >'}>
        <Row {'dataset_id': '< dataset id >', 'uid': '< row_id >'}>


    |

   .. py:method:: delete_rows(self, row_ids)

    Delete multiple rows present inside dataset.

    :param list row_ids: The list of row_ids which is to be deleted.
    :return: returns successful or failure
    :rtype: str

    .. code-block:: python

        dataset.delete_rows(row_ids=["< row id_1 >", "< row id_2 >"])

   |

   .. py:method:: delete(self)

    This method is used to delete a dataset.

    :return: returns successful or failure
    :rtype: str

    .. code-block:: python

        dataset.delete()


    |

   .. py:method:: update_dataset(self, dataset_name, description)

    :param str dataset_name: Name of dataset.
    :param str description: Description of dataset.

    :return: returns a dataset instance.
    :rtype: Dataset

    .. code-block:: python

        dataset = client.get_dataset(dataset_id="<dataset id>")
        dataset.update_dataset(dataset_name="updateddatasetname")

   This prints

    .. code-block:: text

        <Dataset {'dataset_name': 'updateddatasetname', 'dataset_slug': 'image-dataset', 'description': '', 'uid': '855c8a8b-3417-4909-8db2-89f4726fbcf6'}>


    |

