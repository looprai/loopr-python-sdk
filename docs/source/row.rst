==========
Row
==========

.. py:class:: Row()

    Representation of row of a dataset

   .. py:attribute:: uid
    :type: uuid

   |

   .. py:attribute:: dataset_id
    :type: dict

   |

   .. py:method:: delete(self)

    This method is used to delete a row.

    :return: returns successful or failure
    :rtype: str

    .. code-block:: python

        row.delete()
