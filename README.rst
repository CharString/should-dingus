A custom Should-DSL matcher to use with Dingus
===============================================

This modules contains a custom matcher so you can use should_dsl_ with Dingus_ calls

A small warning: The | operator hack of should_dsl's doesn't really go well with the __or__() of a Dingus.
I think the | hack is nasty, and I'm not sure I like should_dsl_ for it. This is where Ruby seems really pretty to me.

.. _should_dsl: http://www.should-dsl.info/
.. _Dingus: http://pypi.python.org/pypi/dingus



You only need to import it ::

    >>> from should_dsl import should, should_not
    >>> from dingus import Dingus
    >>> import should_dingus


------------


**call**

Checks calls on a Dingus ::

    >>> stub = Dingus('stub')
    >>> def some_function():
    ...     stub()
    ...
    >>> some_function |should| call(stub)

*call* can also check that it should be called *once*::

    >>> def some_function():
    ...     stub()
    ...     stub()
    ...
    >>> stub.reset()
    >>> some_function |should| call(stub)
    >>> stub.reset()
    >>> some_function |should| call(stub).once
    Traceback (most recent call last):
    ...
    ShouldNotSatisfied: <Dingus stub> was called 2 times, expected 1

*call* can even check the parameters with *with_params*::

    >>> def some_function():
    ...     stub(True, kwak='tuut', braat='aap')
    ...
    >>> stub.reset()
    >>> some_function |should| call(stub).with_params(True, kwak='tuut', braat='aap')
    >>> stub.reset()
    >>> some_function |should| call(stub).with_params(True, kwak='tuut')
    Traceback (most recent call last):
    ...
    ShouldNotSatisfied: <Dingus stub> has not been called with params (True,) {'kwak': 'tuut'}

*call* *with_params* can be combined with *once*::

    >>> def some_function():
    ...     stub(True, kwak='tuut', braat='aap')
    ...
    >>> stub.reset()
    >>> some_function |should| call(stub).once.with_params(True, kwak='tuut', braat='aap')
    >>> stub.reset()
    >>> some_function |should| call(stub).with_params(True, kwak='tuut', braat='aap').once
