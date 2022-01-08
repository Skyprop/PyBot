
INFO = {
    "version"   :   "1.0",
    "phase"     :   "Alpha",
    "author"    :   "Y.de Vries"
}

import os

def get_version():
    return INFO["version"]

def get_phase():
    return INFO["phase"]

def get_author():
    return INFO["author"]


from pathlib import Path

def get_filename():
    return os.path.basename(Path(__file__).absolute())

def get_filepath():
    return str(Path(__file__).absolute())