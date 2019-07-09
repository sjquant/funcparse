from typing import Tuple
import re


def _parse_params(params: str) -> Tuple[tuple, dict]:
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
            args = tuple([args]) if not isinstance(args, tuple) else args

        kwargs = (eval('dict('+inner_params[start_index:]+')')
                  if start_index is not None else dict())
    return args, kwargs


def parse(word: str) -> Tuple[str, tuple, dict]:
    regexp = r'(\w+)([\(]*.*[\)]*)$'
    match = re.search(regexp, word)

    if bool(match):
        funcname = match.group(1)
        params = match.group(2)
    else:
        raise SyntaxError("Cannot Parse")

    args, kwargs = _parse_params(params)

    return funcname, args, kwargs
