"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

import os
from main_class import DocumentReader

__author__ = "6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "Thanks Mom :)"
__email__ = "nielsheissel99@googlemail.com"



def get_files_in_current_directory():
    files = []
    for file in os.listdir("./"):
        if os.path.isdir(file): 
            file += "/"
        files.append(file)
    # return files.sort(key=lambda x: 0 if x[-1] == "/" else 1)
    return files

def get_parent_directory(directory_path):
    if directory_path == "/":
        return False
    else:
        parent = "/".join(directory_path.split("/")[0:-1])
        if parent == "":
            parent = "/"
        return parent

def check_input(inp):
    try:
        inp = int(inp)
    except:
        inp = "error"
    return inp

def choose_file():
    print_for = lambda n, t: print("("+str(n)+") "+t)
    directory_path = os.getcwd()
    parent_directory = get_parent_directory(directory_path)

    files = get_files_in_current_directory()
    if parent_directory:
        files.insert(0, "<- Parent Directory")
    
    print()
    print("Path:", os.getcwd(), "\n")

    for idx, file in enumerate(files):
        print_for(idx, file)

    print()
    inp = check_input(input("open: "))
    
    if inp == "error":
        print("invalid input")
        return choose_file()

    choosen_file = files[inp]

    if inp == 0 and parent_directory:
        os.chdir(parent_directory)
        return choose_file()
    elif os.path.isdir(choosen_file):
        os.chdir(choosen_file)
        return choose_file()
    else:
        return os.path.abspath(choosen_file)

def main():

    choosen_file = choose_file()

    document_reader = DocumentReader(choosen_file)
    if document_reader.error == "":
        document_reader.write_statistic()
    else:
        print(document_reader.error)


if __name__ == '__main__':
    main()
