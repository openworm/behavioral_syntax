.. behavioral_syntax documentation master file, created by
   sphinx-quickstart on Thu Nov 19 14:34:42 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to behavioral_syntax's documentation!
=============================================

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

The extension methods for the ``IFeatureClass`` and ``ITable`` interfaces that have been added.

+-------------------------------+---------------------------------------------------------------------------------------------------+
| Method                        | Description                                                                                       |
+===============================+===================================================================================================+
| ``IsAssignedClassModelName``  | Used to determine if a class model name(s) has been assigned.                                     |
+-------------------------------+---------------------------------------------------------------------------------------------------+
| ``IsAssignedFieldModelName``  | Used to determine if a field model name(s) has been assigned.                                     |
+-------------------------------+---------------------------------------------------------------------------------------------------+
| ``GetRelationshipClass``      | Used to locate the relationship that has been assigned the class model name(s).                   |
+-------------------------------+---------------------------------------------------------------------------------------------------+
| ``GetRelationshipClasses``    | Used to gather a list of the relationships that has been assigned the class model name(s).        |
+-------------------------------+---------------------------------------------------------------------------------------------------+
| ``GetField``                  | Used to locate the ``IField`` that has been assigned the field model name(s).                     |
+-------------------------------+---------------------------------------------------------------------------------------------------+
| ``GetFields``                 | Used to gather a list of of the ``IField`` objects that has been assigned the field model name(s).|
+-------------------------------+---------------------------------------------------------------------------------------------------+
| ``GetFieldIndex``             | Used to locate the field index that has been assigned the field model name(s).                    |
+-------------------------------+---------------------------------------------------------------------------------------------------+
| ``GetFieldIndexes``           | Used to gather a list of all of the field indexes that has been assigned the field model name(s). |
+-------------------------------+---------------------------------------------------------------------------------------------------+
| ``GetFieldName``              | Used to locate the field name that has been assigned the field model name(s).                     |
+-------------------------------+---------------------------------------------------------------------------------------------------+
| ``GetFieldNames``             | Used to gather a list of all of the field names that has been assigned the field model name(s).   |
+-------------------------------+---------------------------------------------------------------------------------------------------+

The extension methods for the ``IWorkspace`` interface that have been added.

