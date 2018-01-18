"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

import json
from collections import Counter
import re
import tkinter as tk
from tkinter import filedialog

__author__ = "6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "Thanks mom :)"
__email__ = "nielsheissel99@googlemail.com"


class DocumentReader():
    """Simple Class for reading and analyzing documents."""

    def __init__(self, source, type):
        self.source = source
        self.type = type

        self.root = tk.Tk()
        self.root.withdraw()  # maybe not necessary, doesn't work otherwise

        self.filename = filedialog.askopenfilename(parent=self.root)
        print(self.filename)

        self.source = self.filename

        self.encoding = self.find_decoding()

        if self.encoding == "Error":
            print("No valid encoding of document.")
        else:
            self.write_statistic()

        self.root.mainloop

    def find_decoding(self):
        """This method tries all standard encodings and return the working one."""
        try:
            file = open(self.source, encoding="utf-8")
            file.read()
        except UnicodeDecodeError:
            try:
                file = open(self.source, encoding="utf-16")
                file.read()
            except UnicodeDecodeError:
                try:
                    file = open(self.source, encoding="ascii")
                    file.read()
                except UnicodeDecodeError:
                    return "Error"
                return "ascii"
            return "utf-16"
        return "utf-8"

    def read_document(self):
        """A simple method to read and print a document."""
        print("Reading Doc...")
        with open(self.source, encoding=self.encoding) as doc:
            content = doc.read()
            print("Content:\n\n" + content)

    def read_statistic(self):
        """This method analyses the document, and returns a statistic-dictionary"""
        try:
            with open(self.source, encoding=self.encoding) as document:
                content_raw = document.read()

                content = content_raw.replace("\n", " ")
                content = content.replace("  ", " ")
                content = content.replace(",", "")
                content = content.replace(".", "")
                content = content.replace("!", "")
                content = content.replace("–", "")
                content_list = content.split(" ")
                try:  # delete all occurrences of ''
                    while True:
                        content_list.remove("")
                except ValueError:
                    pass

                # document name
                document_name = document.name.split("/")
                document_name = document_name[-1]

                # counter words
                count_dict = dict((x, content_list.count(x)) for x in set(content_list))
                count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)  # sort dict by value
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

                return json_dict
        except FileNotFoundError:
            print("No such File found.")

    def write_statistic(self):
        """This method writes the statistics of a document as a json to a new file."""
        json_dict = self.read_statistic()

        print(json_dict["word_length"])

        destination = self.source.split("/")
        destination_path = ""
        for i in range(len(destination)-1):
            destination_path += "/" + destination[i]
        destination_path += "/statistic_file.txt"

        with open(destination_path, "w", encoding="utf-8") as static_doc:
            json.dump(json_dict, static_doc, ensure_ascii=False, indent=4)

        print("Saved the statistic file under:", destination_path)
