******
Models
******

Model Fields
============

Text fields
-----------
* ``CharField``
* ``TextField``
* ``SlugField``
* ``URLField``

Numeric fields
--------------
* ``DecimalField``
* ``IntegerField``
* ``PositiveIntegerField``
* ``PositiveSmallIntegerField``

Logic fields
------------
* ``BooleanField``

Date and time fields
--------------------
* ``DateField``
* ``DateTimeField``
* ``DurationField``
* ``TimeField``

File fields
-----------
* ``FileField``
* ``ImageField``

Relations
---------
* ``ForeignKeyField``
* ``ManyToManyField``

Model field arguments
=====================

All
---
* ``verbose_name``
* ``max_length``
* ``choices``
* ``validators``
* ``help_text``
* ``null``
* ``blank``
* ``default``
* ``db_index``

Relations
---------
* ``to`` (ForeignKey, ManyToManyField)
* ``related_name`` (ForeignKey, ManyToManyField)
* ``on_delete`` (ForeignKey, ManyToManyField)

Date and time
-------------
* ``auto_add`` (DateField, DateTimeField)
* ``auto_add_now`` (DateField, DateTimeField)

Numeric
-------
* ``decimal_places`` (DecimalField)
* ``max_digits`` (DecimalField)

Abstract Models
===============
.. code-block:: python

    class Meta:
        abstract = True

Architecture
============
* Fat model architecture

Single File vs. Models per file
===============================

Reverse engineering database
============================
* ``python manage.py inspectdb``

Database schema migration
=========================

Makemigrations
--------------
.. code-block:: console

    $ python manage.py makemigrations
    Migrations for 'contact':
      addressbook/contact/migrations/0001_initial.py
        - Create model Contact

Migrate
-------
.. code-block:: console

    $ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, contact, sessions
    Running migrations:
      Applying contact.0001_initial... OK

Example Model
=============
.. literalinclude:: src/django-models-example.py
    :language: python
    :caption: Example Model


Assignments
===========

.. todo:: Convert assignments to literalinclude

Address Book
------------
* Assignment: Address Book
* Complexity: medium
* Lines of code: 50 lines
* Time: 21 min
* Filename: TODO

English:
    .. todo:: English Translation

Polish:
    #. Stwórz projekt ``addressbook``
    #. Stwórz apkę ``contact``
    #. Stwórz model ``Address`` z polami:

        * Typ (do wyboru typ: domowy, praca, komórka)
        * Ulica
        * Numer bloku
        * Numer mieszkania
        * Kod pocztowy
        * Miasto
        * Region
        * Kraj

    #. Stwórz model ``Person`` z polami:

        * Imię
        * Nazwisko
        * Data Urodzenia
        * Zdjęcie
        * Telefon (do wyboru typ: domowy, praca, komórka)
        * Email (do wyboru typ: domowy, praca, komórka)
        * Adres

    #. Osoba może mieć wiele adresów, telefonów i e-maili
    #. Wygeneruj panel administracyjny
    #. Można wypisać kontakty i na głównym ekranie widoczne są podstawowe pola osoby
    #. Dodaj wyszukiwarkę po nazwisku
    #. Dodaj filtrowanie po dacie urodzenia


