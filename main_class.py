"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

import json
import os.path

__author__ = "6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "Thanks mom :)"
__email__ = "nielsheissel99@googlemail.com"


class DocumentReader():
    """Simple Class for reading and analyzing documents."""

    def __init__(self, source_path):
        self.error = ""
        self.document_name = source_path.split("/")[-1]
        self.document_path = "/".join(source_path.split("/")[0:-1])
        self.document_content = self.read_document(source_path)
        if self.error == "":
            self.statistics = self.read_statistic()

    def read_document(self, source_path):
        """This method tries all standard encodings and opens the document with the working one."""
        if (not os.path.isfile(source_path)):
            self.error = "files does not exists"
            return
        try:
            file = open(source_path, "r", encoding="utf-8")
            return file.read()
        except UnicodeDecodeError:
            try:
                file = open(source_path, encoding="utf-16")
                return file.read()
            except UnicodeDecodeError:
                try:
                    file = open(source_path, encoding="ascii")
                    return file.read()
                except UnicodeDecodeError:
                    self.error = "No valid encoding of document."

    def read_statistic(self):
        """This method analyses the document, and returns a statistic-dictionary"""

        content_list = self.document_content.replace("\n", " ") \
            .replace("  ", " ") \
            .replace(",", "") \
            .replace(".", "") \
            .replace("!", "") \
            .replace("–", "") \
            .split(" ")
        try:  # delete all occurrences of '' ?????----------------------------------------------------------------------------------
            while True:
                content_list.remove("")
        except ValueError:
            pass

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
        content_hits = self.document_content.replace("\n", "+")  # enter is one hit
        key_hits = len(content_hits)

        #  number of characters
        content_chars = self.document_content.replace(" ", "")
        content_chars = content_chars.replace("\n", "")
        char_numb = len(content_chars)

        # count characters
        raw_list = list(self.document_content)
        raw_count_dict = dict((x, raw_list.count(x)) for x in set(raw_list))
        raw_count_dict = sorted(raw_count_dict.items(), key=lambda x: x[1], reverse=True)

        json_dict = {"title": self.document_name, "words": word_numb, "key_hits": key_hits,
                     "characters": char_numb, "character_stats": raw_count_dict, "word_stats":
                         word_stats, "word_length": average_word_length}

        return json_dict

    def write_statistic(self):
        """This method writes the statistics of a document as a json to a new file."""
        json_dict = self.statistics

        destination_path = self.document_path + "/statistic_file.json"

        with open(destination_path, "w", encoding="utf-8") as static_doc:
            json.dump(json_dict, static_doc, ensure_ascii=False)

        print("Saved the statistic file under:", destination_path)
