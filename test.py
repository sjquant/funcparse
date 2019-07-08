from funcparse import parse


def test_no_args_no_kwargs():
    word = "func"
    funcname, args, kwargs = parse(word)

    assert funcname == 'func'
    assert args == ()
    assert kwargs == {}

    word = "func()"
    funcname, args, kwargs = parse(word)

    assert funcname == 'func'
    assert args == ()
    assert kwargs == {}


def test_args_no_kwargs():

    word = 'func(1, 2.0, "hello", True, [1,2,3], {"a":1, "b":2}, (1, 2,))'
    funcname, args, kwargs = parse(word)

    assert funcname == 'func'
    assert isinstance(args, tuple)
    assert len(args) == 7
    assert args[0] == 1
    assert args[1] == 2.0
    assert args[2] == "hello"
    assert args[3] is True
    assert args[4] == [1, 2, 3]
    assert args[5] == {'a': 1, 'b': 2}
    assert args[6] == (1, 2)
    assert kwargs == {}


def test_no_args_kwargs():

    word = ('func(a=1, b=2.0, c="hello", d=True, '
            'e=[1, 2, 3], f={"a":1, "b":2}, g=(1, 2,))')
    funcname, args, kwargs = parse(word)

    assert funcname == 'func'
    assert args == ()
    assert isinstance(kwargs, dict)

    assert len(kwargs) == 7
    assert kwargs['a'] == 1
    assert kwargs['b'] == 2.0
    assert kwargs['c'] == 'hello'
    assert kwargs['d'] is True
    assert kwargs['e'] == [1, 2, 3]
    assert kwargs['f'] == {'a': 1, 'b': 2}
    assert kwargs['g'] == (1, 2)


def test_args_kwargs():
    word = ('func(1, 2.0, "hello", True, [1,2,3], {"a":1, "b":2}, (1, 2), '
            'a=1, b=2.0, c="hello", d=True, '
            'e=[1, 2, 3], f={"a": 1, "b": 2}, g=(1, 2,))')
    funcname, args, kwargs = parse(word)

    assert funcname == 'func'
    assert isinstance(args, tuple)
    assert len(args) == 7
    assert args[0] == 1
    assert args[1] == 2.0
    assert args[2] == "hello"
    assert args[3] is True
    assert args[4] == [1, 2, 3]
    assert args[5] == {'a': 1, 'b': 2}
    assert args[6] == (1, 2)
    assert isinstance(kwargs, dict)
    assert len(kwargs) == 7
    assert kwargs['a'] == 1
    assert kwargs['b'] == 2.0
    assert kwargs['c'] == 'hello'
    assert kwargs['d'] is True
    assert kwargs['e'] == [1, 2, 3]
    assert kwargs['f'] == {'a': 1, 'b': 2}
    assert kwargs['g'] == (1, 2)
