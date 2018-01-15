"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

import json

__author__ = "6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "Thanks Mom :)"
__email__ = "nielsheissel99@googlemail.com"


class DocumentReader():
    """Simple Class"""
    test_var = 2

    def __init__(self, source, type):
        self.source = source
        self.type = type

    def test_methode(self):
        print("Test")

        if self.type is True:
            print("was true!")
        else: print("was false.")
