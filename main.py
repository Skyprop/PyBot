import os
from pathlib import Path

#custom
import conf
import file_properties

class __FILEPROPERTIES__:
    def __init__(self):

        self.VERSION = file_properties.get_version()
        self.AUTHOR = file_properties.get_author()

        self.FILENAME = os.path.basename(Path(__file__).absolute())
        self.FULLPATH = str(Path(__file__).absolute())
        self.DIRECTORY = Path().absolute()
        
def main():

    #fileproperties instance, some properties can be changed in properties.py
    FILEPROPERTIES = __FILEPROPERTIES__()

    #explorer instance
    explorer = file_properties.explorer()
    file_properties.debugprint("Hello "+explorer.get_username()+"")

    #autoupdater instance, can be enabled/disabled in properties.py
    AUTOUPDATER = file_properties.updateManager(FILEPROPERTIES.FULLPATH)

if __name__ == "__main__":
    main()