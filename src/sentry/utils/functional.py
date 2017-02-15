from __future__ import absolute_import

import functools

from django.utils.functional import empty


def extract_lazy_object(lo):
    """
    Unwrap a LazyObject and return the inner object. Whatever that may be.

    ProTip: This is relying on `django.utils.functional.empty`, which may
    or may not be removed in the future. It's 100% undocumented.
    """
    if not hasattr(lo, '_wrapped'):
        return lo
    if lo._wrapped is empty:
        lo._setup()
    return lo._wrapped


def apply_values(function, mapping):
    keys, values = zip(*mapping.items())
    return dict(zip(keys, function(values)))


def map_values(function, mapping):
    return apply_values(
        functools.partial(map, function),
        mapping,
    )
