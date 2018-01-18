"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

import tkinter as tk
from tkinter import filedialog
from main_class import DocumentReader

__author__ = "6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "Thanks Mom :)"
__email__ = "nielsheissel99@googlemail.com"


def main():

    root = tk.Tk()
    root.withdraw()  # probably not necessary

    filename = filedialog.askopenfilename(parent=root)
    document_reader = DocumentReader(filename)
    if document_reader.error == "":
        document_reader.write_statistic()
    else:
        print(document_reader.error)

    root.mainloop


if __name__ == '__main__':
    main()
