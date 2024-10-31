seshat.apps.core.management.commands.populate_gadm
==================================================

.. py:module:: seshat.apps.core.management.commands.populate_gadm


Classes
-------

.. autoapisummary::

   seshat.apps.core.management.commands.populate_gadm.Command


Module Contents
---------------

.. py:class:: Command(stdout=None, stderr=None, no_color=False, force_color=False)

   Bases: :py:obj:`django.core.management.base.BaseCommand`


   The base class from which all management commands ultimately
   derive.

   Use this class if you want access to all of the mechanisms which
   parse the command-line arguments and work out what code to call in
   response; if you don't need to change any of that behavior,
   consider using one of the subclasses defined in this file.

   If you are interested in overriding/customizing various aspects of
   the command-parsing and -execution behavior, the normal flow works
   as follows:

   1. ``django-admin`` or ``manage.py`` loads the command class
      and calls its ``run_from_argv()`` method.

   2. The ``run_from_argv()`` method calls ``create_parser()`` to get
      an ``ArgumentParser`` for the arguments, parses them, performs
      any environment changes requested by options like
      ``pythonpath``, and then calls the ``execute()`` method,
      passing the parsed arguments.

   3. The ``execute()`` method attempts to carry out the command by
      calling the ``handle()`` method with the parsed arguments; any
      output produced by ``handle()`` will be printed to standard
      output and, if the command is intended to produce a block of
      SQL statements, will be wrapped in ``BEGIN`` and ``COMMIT``.

   4. If ``handle()`` or ``execute()`` raised any exception (e.g.
      ``CommandError``), ``run_from_argv()`` will  instead print an error
      message to ``stderr``.

   Thus, the ``handle()`` method is typically the starting point for
   subclasses; many built-in commands and command types either place
   all of their logic in ``handle()``, or perform some additional
   parsing work in ``handle()`` and then delegate from it to more
   specialized methods as needed.

   Several attributes affect behavior at various steps along the way:

   ``help``
       A short description of the command, which will be printed in
       help messages.

   ``output_transaction``
       A boolean indicating whether the command outputs SQL
       statements; if ``True``, the output will automatically be
       wrapped with ``BEGIN;`` and ``COMMIT;``. Default value is
       ``False``.

   ``requires_migrations_checks``
       A boolean; if ``True``, the command prints a warning if the set of
       migrations on disk don't match the migrations in the database.

   ``requires_system_checks``
       A list or tuple of tags, e.g. [Tags.staticfiles, Tags.models]. System
       checks registered in the chosen tags will be checked for errors prior
       to executing the command. The value '__all__' can be used to specify
       that all system checks should be performed. Default value is '__all__'.

       To validate an individual application's models
       rather than all applications' models, call
       ``self.check(app_configs)`` from ``handle()``, where ``app_configs``
       is the list of application's configuration provided by the
       app registry.

   ``stealth_options``
       A tuple of any options the command uses which aren't defined by the
       argument parser.


   .. py:method:: add_arguments(parser)

      Entry point for subclassed commands to add custom arguments.



   .. py:method:: handle(*args, **options)

      The actual logic of the command. Subclasses must implement
      this method.



   .. py:attribute:: help
      :value: 'Populates the GADMShapefile table with features from a GeoPackage'



