"""Perform compliance analysis on materials data stored in Granta MI."""

from ._connection import Connection
from ._exceptions import GrantaMIException

__version__ = "0.1.0dev"
# TODO use STK to extend BoM services objects? e.g. adding all references to sparsely referenced object
