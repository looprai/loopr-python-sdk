=======
Dataset
=======

.. py:class:: Dataset()

    Dataset is a collection of rows containing data. One Dataset may consists of several rows.
        Type of Datasets :
            - image
            - text
            - sku
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

   .. py:method:: add_row(self, **kwargs)
    Adds rows to dataset

    :return: returns a Row instance
    :rtype: Row

    .. code-block:: python

        image_dataset = client.get_dataset(dataset_id="<dataset_id>")
        image_row= image_dataset.add_row(data={"image_url":"gs://loopr-demo-dataset/a61a69be-f152-4175-bab4-e119f980bc3d"})
        paired_dataset = client.get_dataset(dataset_id="<dataset_id>")
        paired_row= image_dataset.add_row(query={"text":"query text"}, data={"sku_image": "gs://loopr-demo-dataset/test_image.jpeg","sku_name":"product name"})

        print(image_row)
        print(paired_row)

    This prints

    .. code-block:: text

        <ImageRow {'dataset_id': '< dataset id >', 'uid': '< row id >'}>
        <PairedRow {'dataset_id': '< dataset id >', 'uid': '< row_id >'}>


    |

   .. py:method:: delete_rows(self, row_ids)

   Delete multiple rows present inside dataset.

    :return: returns successful or failure
    :rtype: str

    .. code-block:: python

        dataset.delete_rows(row_ids=["< row id_1 >, < row id_2 >"])

   |

   .. py:method:: delete(self)

   This method is used to delete a dataset.

    :return: returns successful or failure
    :rtype: str

    .. code-block:: python

        dataset.delete()
