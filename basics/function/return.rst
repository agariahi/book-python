.. _Function Return:

***************
Function Return
***************


Syntax
======
.. code-block:: python

    def my_function():
        return <expression>

.. code-block:: python

    def mean():
        return (1+2) / 2

.. code-block:: python

    def add():
        a = 1
        b = 2
        return a + b


Return Keyword
==============
* ``return`` keyword indicates outcome of the function
* Code after ``return`` will not execute

.. code-block:: python

    def hello():
        return 'ehlo world'

    print(hello())
    # 'ehlo world'

.. code-block:: python

    def hello():
        return 'ehlo world'
        print('This will not be executed')

    print(hello())
    # 'ehlo world'


Return Basic Type
=================
.. code-block:: python

    def my_function():
        return 42

.. code-block:: python

    def my_function():
        return 13.37

.. code-block:: python

    def my_function():
        return 'Mark Watney'

.. code-block:: python

    def my_function():
        return True


Return Sequence
===============
.. code-block:: python

    def my_function():
        return list([42, 13.37, 'Mark Watney'])

    def my_function():
        return [42, 13.37, 'Mark Watney']

.. code-block:: python

    def my_function():
        return tuple((42, 13.37, 'Mark Watney'))

    def my_function():
        return (42, 13.37, 'Mark Watney')

    def my_function():
        return 42, 13.37, 'Mark Watney'

.. code-block:: python

    def my_function():
        return set({42, 13.37, 'Mark Watney'})

    def my_function():
        return {42, 13.37, 'Mark Watney'}

.. code-block:: python

    def my_function():
        return frozenset({42, 13.37, 'Mark Watney'})


Return Mapping
==============
.. code-block:: python

    def my_function():
        return dict(firstname='Mark', lastname='Watney')

    def my_function():
        return {'firstname': 'Mark', 'lastname': 'Watney'}


Return Nested Sequence
======================
.. code-block:: python

    def my_function():
        return [
            ('Mark', 'Watney'),
            {'Jan Twardowski', 'Melissa Lewis'},
            {'astro': 'Иванович', 'agency': {'name': 'Roscosmos'}},
            {'astro': 'Jiménez', 'missions': ('Mercury', 'Gemini', 'Apollo')},
            {'astro': 'Vogel', 'missions': (list(), tuple(), set(), frozenset())},
        ]


Return None
===========
* Python will ``return None`` if no explicit return is specified

.. code-block:: python

    def my_function():
        return None

.. code-block:: python

    def my_function():
        print('ehlo world')

.. code-block:: python

    def my_function():
        pass

.. code-block:: python

    def my_function():
        """My function"""


Intercept returned value
========================
.. code-block:: python

    def my_function():
        return 1


    result = my_function()
    print(result)
    # 1


Assignments
===========

.. literalinclude:: assignments/function_return_numbers.py
    :caption: :download:`Solution <assignments/function_return_numbers.py>`
    :end-before: # Solution
