from typing import Any
import functools


def type_check(*allowed_types):
    def decorator(method):
        @functools.wraps(method)
        def check_types(*args, **kwargs):
            values = list(args) + list(kwargs.values())

            if len(allowed_types) != len(values):
                raise ValueError(
                    f"Number of types ({len(allowed_types)}) does not match number of arguments ({len(values)})"
                )
            for value, allowed_type in zip(values, allowed_types):
                try:
                    check_type(value, allowed_type)
                except AssertionError:
                    raise TypeError(
                        f'Incorrect type for value "{value}". Expected "{allowed_type}"'
                    )
            return method(*args, **kwargs)

        return check_types

    return decorator


def check_type(obj, allowed_type):
    if allowed_type == Any:
        return
    if isinstance(allowed_type, list):
        assert isinstance(obj, list)
        for value, mytype in zip(obj, allowed_type):
            check_type(value, mytype)
    elif isinstance(allowed_type, tuple):
        assert isinstance(obj, tuple)
        for value, mytype in zip(obj, allowed_type):
            check_type(value, mytype)
    else:
        assert isinstance(obj, allowed_type)
    return
