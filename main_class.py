"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

import json
from collections import Counter
import re

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
        choice = input("Y/N")
        if choice == "Y":
            self.read_document()
        else: print("You selected no.")

    def read_document(self):
        print("Reading Doc...")
        with open(self.source, encoding="utf-16") as document:
            print(document.name)
            content = document.read()
            content = content.replace("\n", " ")
            content = content.replace("  ", " ")
            content = content.replace(",", "")
            content = content.replace(".", "")
            content = content.replace("!", "")
            content_list = content.split(" ")


            print(content_list)
            # counter
            count_dict = dict((x,content_list.count(x)) for x in set(content_list))
            count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
            print(count_dict)

            print(Counter(content_list))
            print("Content:", content)

