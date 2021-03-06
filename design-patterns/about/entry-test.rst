**********
Entry Test
**********


Entry Test Listdict
===================
* Assignment: Entry Test Listdict
* Complexity: easy
* Lines of code: 8 lines
* Time: 13 min
* Filename: entry_test_listdict.py

English:
    #. Use data from "Given" section (see below)
    #. Separate header and data
    #. Print ``result: list[dict]``

        * key - name from the header
        * value - measurement or species

    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Odseparuj nagłówek i dane
    #. Wypisz ``result: list[dict]``

        * klucz: nazwa z nagłówka
        * wartość: wyniki pomiarów lub gatunek

    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
                (5.8, 2.7, 5.1, 1.9, 'virginica'),
                (5.1, 3.5, 1.4, 0.2, 'setosa'),
                (5.7, 2.8, 4.1, 1.3, 'versicolor'),
                (6.3, 2.9, 5.6, 1.8, 'virginica'),
                (6.4, 3.2, 4.5, 1.5, 'versicolor'),
                (4.7, 3.2, 1.3, 0.2, 'setosa'),
                (7.0, 3.2, 4.7, 1.4, 'versicolor'),
                (7.6, 3.0, 6.6, 2.1, 'virginica'),
                (4.9, 3.0, 1.4, 0.2, 'setosa'),
                (4.9, 2.5, 4.5, 1.7, 'virginica'),
                (7.1, 3.0, 5.9, 2.1, 'virginica'),
                (4.6, 3.4, 1.4, 0.3, 'setosa'),
                (5.4, 3.9, 1.7, 0.4, 'setosa'),
                (5.7, 2.8, 4.5, 1.3, 'versicolor'),
                (5.0, 3.6, 1.4, 0.3, 'setosa'),
                (5.5, 2.3, 4.0, 1.3, 'versicolor'),
                (6.5, 3.0, 5.8, 2.2, 'virginica'),
                (6.5, 2.8, 4.6, 1.5, 'versicolor'),
                (6.3, 3.3, 6.0, 2.5, 'virginica'),
                (6.9, 3.1, 4.9, 1.5, 'versicolor'),
                (4.6, 3.1, 1.5, 0.2, 'setosa')s]

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
     {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
     {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
     ...]


Entry Test Nested
=================
* Assignment: Entry Test Nested
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min
* Filename: entry_test_nested.py

English:
    #. Use data from "Given" section (see below)
    #. Separate header from data
    #. Iterate over data
    #. Print species names ending with "ica" or "sa"

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Oddziel nagłówek od danych
    #. Iteruj po danych
    #. Wypisz nazwy gatunków kończące się na "ica" lub "sa"

Given:
    .. code-block:: python

        DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
                (5.8, 2.7, 5.1, 1.9, {'virginica'}),
                (5.1, 3.5, 1.4, 0.2, {'setosa'}),
                (5.7, 2.8, 4.1, 1.3, {'versicolor'}),
                (6.3, 2.9, 5.6, 1.8, {'virginica'}),
                (6.4, 3.2, 4.5, 1.5, {'versicolor'}),
                (4.7, 3.2, 1.3, 0.2, {'setosa'}),
                (7.0, 3.2, 4.7, 1.4, {'versicolor'}),
                (7.6, 3.0, 6.6, 2.1, {'virginica'}),
                (4.6, 3.1, 1.5, 0.2, {'setosa'})]


Entry Test Hosts
================
* Assignment: Entry Test Hosts
* Complexity: medium
* Lines of code: 15 lines
* Time: 13 min
* Filename: entry_test_hosts.py

English:
    #. Use data from "Given" section (see below)
    #. Save input data to file ``hosts.txt``
    #. Copy also comments and empty lines
    #. For each line in file:

        #. Skip line if it's empty, is whitespace or starts with comment ``#``
        #. Remove leading and trailing whitespaces
        #. Split line by whitespace
        #. Separate IP address and hosts names
        #. Use one line ``if`` to check whether dot ``.`` is in the IP address
        #. If is present then protocol is IPv4 otherwise IPv6
        #. Append IP address and hosts names to ``result: list[dict]``

    #. Merge hostnames for the same IP
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Zapisz dane wejściowe do pliku ``hosts.txt``
    #. Skopiuj również komentarz i pustą linię
    #. Dla każdej lini w pliku:

        #. Pomiń linię jeżeli jest pusta, jest białym znakiem lub zaczyna się od komentarza ``#``
        #. Usuń białe znaki na początku i końcu linii
        #. Podziel linię po białych znakach
        #. Odseparuj adres IP i nazwy hostów
        #. Wykorzystaj jednolinikowego ``if`` do sprawdzenia czy jest kropka ``.`` w adresie IP
        #. Jeżeli jest obecna to protokół  jest IPv4, w przeciwnym przypadku IPv6
        #. Dodaj adres IP i nazwy hostów do ``result: list[dict]``

    #. Scal nazwy hostów dla tego samego IP
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: text

        ##
        # ``/etc/hosts`` structure:
        #   - IPv4 or IPv6
        #   - Hostnames
         ##

        127.0.0.1       localhost
        127.0.0.1       astromatt
        10.13.37.1      nasa.gov esa.int roscosmos.ru
        255.255.255.255 broadcasthost
        ::1             localhost

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'ip': '127.0.0.1', 'protocol': 'ipv4', 'hostnames': {'localhost', 'astromatt'}},
     {'ip': '10.13.37.1', 'protocol': 'ipv4', 'hostnames': {'nasa.gov', 'esa.int', 'roscosmos.ru'}},
     {'ip': '255.255.255.255', 'protocol': 'ipv4', 'hostnames': {'broadcasthost'}},
     {'ip': '::1', 'protocol': 'ipv6', 'hostnames': {'localhost'}}]

Hints:
    * ``str.isspace()``
    * ``value = True if ... else False``
