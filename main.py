"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

import json
import main_class

__author__ = "6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "Thanks Mom :)"
__email__ = "nielsheissel99@googlemail.com"



def main():
    source = "/Users/nielsheissel/Downloads/Morgen_Kinder.txt"

    print("Let's start the program.")
    test_instance = main_class.DocumentReader(source, False)

if __name__ == '__main__':
    main()
