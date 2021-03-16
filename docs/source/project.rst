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

        <Annotation {'annotation_data': {'taxonomies': [{'taxonomy_name': 'relevancy', 'value': ['3'], 'annotated_by': 'test@loopr.com', 'last_updated_by': 'test@loopr.com'}]}, 'row': {'payload': [{'image_url': 'https://dev-storage.loopr.ai/loopr-dev-payloads/test_loopr.jpeg', 'text': 'Drobo Portable Hard Drive Case', 'website': None, 'meta': {'width': 320, 'height': 320}}], 'query': 'portable hard drive', 'payload_type': 'text_sku'}, 'submitted_at': datetime.datetime(2020, 11, 19, 10, 51, 49, 159000, tzinfo=datetime.timezone.utc), 'uid': 'a3b82786-1995-4788-9b03-3b2906cc70ee'}>
        <Annotation {'annotation_data': {'taxonomies': [{'taxonomy_name': 'relevancy', 'value': ['3'], 'annotated_by': 'test@loopr.com', 'last_updated_by': 'test@loopr.com'}]}, 'row': {'payload': [{'image_url': 'https://dev-storage.loopr.ai/loopr-dev-payloads/test_loopr.jpeg', 'text': 'Mobile Edge Portable Hard Drive Carrying Case (Small, Black)', 'website': None, 'meta': {'width': 320, 'height': 320}}], 'query': 'portable hard drive', 'payload_type': 'text_sku'}, 'submitted_at': datetime.datetime(2020, 11, 19, 10, 51, 52, 976000, tzinfo=datetime.timezone.utc), 'uid': '487a4280-94b7-4a1d-95f9-eebc68f8800f'}>

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
        project.add_taxonomy(taxonomy="{taxonomy data}")


    |

   .. py:method:: update_taxonomy(self, taxonomy)

    :param dict taxonomy: Taxonomy/Configuration of project.

    :return: returns successful or failure
    :rtype: str

    .. code-block:: python

        project = client.update_project(project_id="<project id>")
        project.update_taxonomy(taxonomy="{taxonomy data}")


    |