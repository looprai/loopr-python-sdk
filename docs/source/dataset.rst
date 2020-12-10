=======
Dataset
=======

.. py:class:: Dataset()

    Dataset is a collection of rows containing data. One Dataset may consists of several rows.
        Type of Datasets :
            - image
            - paired (text_image/image_image/text_sku/image_sku)

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
                    ``data={"image_url":"< image_url >"}``
                * text_image:
                    ``query={"text":"<your query>"}, data={"image":"<image_url>"}``
                * image_image:
                    ``query={"image":"<your query image>"}, data={"image":"<image_url>"}``
                * text_sku:
                    ``query={"text":"<your query>"}, data={"sku_image":"<image_url>", "sku_name":"<name>"}``
                * image_sku:
                    ``query={"image":"<your query image>"}, data={"sku_image":"<image_url>", "sku_name":"<name>"}``
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

    :param str external_id: (Optional) An unique field that a user can provide to represent rows.

    :return: returns a Row instance
    :rtype: Row

    .. code-block:: python

        image_dataset = client.get_dataset(dataset_id="<dataset_id>")
        image_row= image_dataset.add_row(data={"image_url":"gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d"})
        paired_dataset = client.get_dataset(dataset_id="<dataset_id>")
        paired_row= image_dataset.add_row(query={"text":"query text"}, data={"sku_image": "gs://loopr-demo-dataset/test_image.jpeg","sku_name":"product name"})
        text_dataset = client.get_dataset(dataset_id="<dataset_id>")
        text_row = text_dataset.add_row(data={"text":"text data"})
        sku_dataset = client.get_dataset(dataset_id="<dataset_id>")
        sku_row = sku_dataset.add_row(data={"sku_image": "gs://loopr-demo-dataset/a7e9b922-f8d5-43aa-abb9-5a3095f88edc","sku_name": "product name"})

        print(image_row)
        print(paired_row)
        print(text_row)
        print(sku_row)

    This prints

    .. code-block:: text

        <ImageRow {'dataset_id': '< dataset id >', 'uid': '< row id >'}>
        <PairedRow {'dataset_id': '< dataset id >', 'uid': '< row_id >'}>
        <TextRow {'dataset_id': '< dataset id >', 'uid': '< row_id >'}>
        <SkuRow {'dataset_id': '< dataset id >', 'uid': '< row_id >'}>


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
