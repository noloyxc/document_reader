"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

import json
from collections import Counter
import re
import tkinter as tk
from tkinter import filedialog

__author__ = "6770541: Niels Heissel, 0000000: Philipp Heinz"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "Thanks Mom :)"
__email__ = "nielsheissel99@googlemail.com"


def read_statistic(source):
    with open(source, encoding="utf-16") as document:
            content_raw = document.read()
            content = content_raw.replace("\n", " ")
            content = content.replace("  ", " ")
            content = content.replace(",", "")
            content = content.replace(".", "")
            content = content.replace("!", "")
            content = content.replace("–", "")
            content_list = content.split(" ")
            try:
                while True:
                    content_list.remove("")
            except ValueError:
                pass

            # document name
            document_name = document.name.split("/")
            document_name = document_name[-1]

            # counter words
            count_dict = dict((x, content_list.count(x)) for x in set(content_list))
            count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
            word_stats = count_dict

            # number of words
            word_numb = len(content_list)

            # average word length
            total_word_length = 0
            for word in content_list:
                total_word_length += len(word)
            average_word_length = total_word_length / len(content_list)

            # hits
            content_hits = content_raw.replace("\n", "+")  # enter is one hit
            key_hits = len(content_hits)

            #  number of characters
            content_chars = content_raw.replace(" ", "")
            content_chars = content_chars.replace("\n", "")
            char_numb = len(content_chars)

            # count characters
            raw_list = list(content_raw)
            raw_count_dict = dict((x, raw_list.count(x)) for x in set(raw_list))
            raw_count_dict = sorted(raw_count_dict.items(), key=lambda x: x[1], reverse=True)

            json_dict = {"title": document_name, "words": word_numb, "key_hits": key_hits,
                         "characters": char_numb, "character_stats": raw_count_dict, "word_stats":
                             word_stats, "word_length": average_word_length}

            print(json_dict)
