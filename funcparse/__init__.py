import re


def _parse_params(params: str, object_params: bool = False):
    if params == '' or params == '()':
        args: tuple = ()
        kwargs: dict = {}
    else:
        inner_params = params[1: -1]
        match = re.search(r'\w+\s*=.+', inner_params)
        start_index = match.start() if bool(match) else None  # type:ignore

        if start_index == 0:
            args = ()
        else:
            args = eval(inner_params[: start_index])

        kwargs = (eval('dict('+inner_params[start_index:]+')')
                  if start_index is not None else dict())
    return args, kwargs


def parse(word, object_params=False):
    regexp = r'(\w+)([\(]*.*[\)]*)$'
    match = re.search(regexp, word)

    funcname = match.group(1)
    params = match.group(2)
    try:
        args, kwargs = _parse_params(params, object_params)
    except SyntaxError:
        raise

    return funcname, args, kwargs
