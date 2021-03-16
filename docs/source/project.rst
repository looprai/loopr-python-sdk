=======
Project
=======

.. py:class:: Project()

   Loopr Projects are a way of organizing similar tasks, so that one can share parameters among tasks.
   A project can attach multiple datasets.
   Type of Loopr Projects:

        * object_detection
        * relevancy
        * categorization

   .. py:attribute:: uid
    :type: uuid

   |

   .. py:attribute:: project_name
    :type: str

   |

   .. py:attribute:: project_slug
    :type: str

   |

   .. py:attribute:: project_type
    :type: str

   |

   .. py:attribute:: dataset_type
    :type: str

   |

   .. py:method:: delete(self)

    This method is used to delete a project.

    :return: returns successful or failure
    :rtype: str

    .. code-block:: python

        project.delete()

   |

   .. py:method:: export_configuration(self)

   This returns a download url of project configuration.

   :return: returns a url
   :rtype: str

    .. code-block:: python

     download_url= project.export_configuration()

    |

   .. py:method:: get_annotations(self, offset=0, **kwargs)

    :param float offset: (Optional) The offset from which to fetch annotations.
    :param datetime start_date: (Optional) The start range of annotations.
    :param datetime end_date: (Optional) The end range of annotations.
    :param list external_ids: (Optional) The external_ids to filter.
    :param list group_ids: (Optional) The external_ids to filter.
    :param list review: (Optional) The list of review flags:
                                                * not_reviewed
                                                * negative
                                                * positive
    :param str sort_key: (Optional) The key to sort the annotations.
                            default - date
    :param str sort_by: (Optional) The order to sort by.
                        Default - ascending

    :return: returns an iterable loopr annotaion instance
    :rtype: Annotation

    .. code-block:: python

        project = client.get_project(project_id="<project id>")
        for annotation in project.get_annotations():
            print(annotation)

   This prints

    .. code-block:: text

        <Annotation {'annotation_data': {'classifications': [{'concept_id': 'c_id1', 'annotated_by': 'test@loopr.com', 'classification_name': 'How well does this query match result?', 'choices': [{'choice_id': 'choice_id1', 'name': '3', 'description': 'Good'}]}], 'row': {'payload_type': 'text', 'external_id': 'external_id1', 'payload': [{'image_url': 'https://dev-storage.loopr.ai/loopr-dev-payloads/test_loopr1.jpeg', 'meta': {'width': 700, 'height': 700}, 'image_thumbnail': 'https://dev-storage.loopr.ai/loopr-dev-payloads/test_loopr1.jpeg'}], 'query': 'query1'}, 'submitted_at': datetime.datetime(2021, 1, 19, 11, 2, 13, 208000, tzinfo=datetime.timezone.utc), 'uid': '30266846-f48f-4a2d-83d1-cca57b93c816'}>
        <Annotation {'annotation_data': {'classifications': [{'concept_id': 'c_id2', 'annotated_by': 'test@loopr.com', 'classification_name': 'How well does this query match result?', 'choices': [{'choice_id': 'choice_id2', 'name': '4', 'description': 'Excellent'}]}], 'row': {'payload_type': 'text', 'external_id': 'external_id2', 'payload': [{'image_url': 'https://dev-storage.loopr.ai/loopr-dev-payloads/test_loopr2.jpeg', 'meta': {'width': 780, 'height': 600}, 'image_thumbnail': 'https://dev-storage.loopr.ai/loopr-dev-payloads/test_loopr2.jpeg'}], 'query': 'query2'}, 'submitted_at': datetime.datetime(2021, 1, 19, 11, 2, 13, 208000, tzinfo=datetime.timezone.utc), 'uid': '30266846-f48f-4a2d-83d1-cca57b93c816'}>

    |

   .. py:method:: attach_dataset(self, dataset_ids)

    :param list dataset_ids: The list of dataset_ids to be attached.

    :return: returns successful or failure
    :rtype: str

    .. code-block:: python

        project = client.get_project(project_id="<project id>")
        project.attach_dataset(dataset_ids=["<dataset_id>", ...])


    |

   .. py:method:: update_project(self, project_name, description)

    :param str project_name: Name of project.
    :param str description: Description of project.

    :return: returns a project instance.
    :rtype: Project

    .. code-block:: python

        project = client.get_project(project_id="<project id>")
        project.update_project(project_name="updatedprojectname")

   This prints

    .. code-block:: text

        <Project {'description': None, 'project_name': 'updatedprojectname', 'project_slug': 'categorization-project', 'project_type': 'categorization', 'uid': '30266846-f48f-4a2d-83d1-cca57b93c816'}>


    |

   .. py:method:: add_taxonomy(self, taxonomy)

    :param dict taxonomy: Taxonomy/Configuration of project.

    :return: returns successful or failure
    :rtype: str

    .. code-block:: python

        project = client.get_project(project_id="<project id>")
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


    |

   .. py:method:: update_taxonomy(self, taxonomy)

    :param dict taxonomy: Taxonomy/Configuration of project.

    :return: returns updated taxonomy data
    :rtype: str

    .. code-block:: python

        project = client.update_project(project_id="<project id>")
        project.update_taxonomy(taxonomy="{taxonomy data}")


    |

   .. py:method:: get_taxonomy(self)

    :return: returns taxonomy data
    :rtype: str

    .. code-block:: python

        project = client.update_project(project_id="<project id>")
        project.get_taxonomy()


    |