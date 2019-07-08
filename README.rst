funcparse
=========

Introduction
------------
Parse `funcname`, `args`, `kargs` from function-like string

Installation
------------

``pip install funcparse``

Example
--------

.. code:: python

    from funcparse import parse

    funcname, args, kwargs = parse('say(1, 2, "Hello", a=1, b=2, c="World")')

    print(funcname)
    # >>> 'say'

    print(args)
    # >>> (1, 2, 'Hello')

    print(kwargs)
    # >>> {'a': 1, 'b': 2, 'c': 'World'}

.. note::

    It cannot parse another object(i.e. dict) with '=' args in it as follows.

.. code:: python

    from funcparse import parse

    # Raise Syntax Error
    # Use {"from": "a", "to": "b"} instead.
    funcname, args, kwargs = parse('hi(dict(from="a", to="b"))')
