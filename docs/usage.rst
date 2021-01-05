=====
Usage
=====

To use ACDH Django Vocabs in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'vocabs.apps.VocabsConfig',
        ...
    )

Add ACDH Django Vocabs's URL patterns:

.. code-block:: python

    from vocabs import urls as vocabs_urls


    urlpatterns = [
        ...
        url(r'^', include(vocabs_urls)),
        ...
    ]
