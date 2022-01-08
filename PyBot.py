import os
from pathlib import Path

#custom
import info
import AutoUpdater

AutoUpdater.debug()

class __FILEPROPERTIES__:
    def __init__(self):

        self.VERSION = info.get_version()
        self.PHASE = info.get_phase()
        self.AUTHOR = info.get_author()

        self.FILENAME = os.path.basename(Path(__file__).absolute())
        self.DIRECTORY = str(Path(__file__).absolute())

    def CD_BACK(self, count):
        for I in range(count):
            self.DIRECTORY = self.DIRECTORY[0:len(self.DIRECTORY)-len(self.FILENAME)]

def main():

    FILEPROPERTIES = __FILEPROPERTIES__()
    print(FILEPROPERTIES.VERSION)


if __name__ == "__main__":
    main()