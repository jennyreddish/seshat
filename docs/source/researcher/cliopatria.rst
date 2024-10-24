Cliopatria polity borders dataset
=================================

Cliopatria is a comprehensive open-source geospatial dataset of worldwide states, political groups, events, and rulers from 3400BCE to 2024CE.
It is part of the Seshat Global History Databank project.
Presently it comprises over 1800 political entities sampled at varying timesteps and spatial scales.
Cliopatria is available as part of the Seshat database and API and is used on the `World Map <https://seshat-db.com/core/world_map>`_ and polity pages of the Seshat website.

Working with the Cliopatria borders dataset
--------------------------------------------

Cliopatria is available as a stand-alone dataset which is stored and documented at `github.com/Seshat-Global-History-Databank/cliopatria <https://github.com/Seshat-Global-History-Databank/cliopatria>`_.
The data takes the form of a single GeoJSON file, a format that can be loaded by a wide variety of software for handling geospatial data.
Whilst Cliopatria can be accessed via the `Seshat API <api.rst>`_, in most cases it is faster and more convenient to download the dataset directly from the GitHub repository and work with it locally.

A great way to get started exploring the Cliopatria dataset is to open it in the Jupyter notebook examples found inside the `github.com/Seshat-Global-History-Databank/cliopatria <https://github.com/Seshat-Global-History-Databank/cliopatria>`_ GitHub repo.
The `notebooks` folder contains a processing script to add colors to the dataset, alongside a notebook which loads the data in GeoPandas and includes an interactive Folium plot.
There is also a notebook which loads Cliopatria and plots some stats about the dataset.
Follow the README instructions in the `notebooks` folder.

.. tip::

    You may want to start by reading the `Software tools <software-tools>`_ page to ensure you have Python and Git installed on your computer.


Cliopatria edit and release process
-----------------------------------

Instructions for downloading, using and making new releases the dataset are available at the `Cliopatria GitHub repository <https://github.com/Seshat-Global-History-Databank/cliopatria>`_.