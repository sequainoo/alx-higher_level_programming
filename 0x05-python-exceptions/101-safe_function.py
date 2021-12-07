#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except BaseException as e:
        stderr.write('Exception: {}\n'.format(e))
        res = None
    finally:
        return res
