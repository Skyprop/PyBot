import conf
import requests
import os
from zipfile import ZipFile
from pathlib import Path
import glob
from tkinter import messagebox
from pygame import mixer

def get_git_api(single_api):
    try:
        return requests.get(conf.GIT_API_LATEST, auth=(conf.GIT_USERNAME, conf.GIT_API_TOKEN)).json()[single_api]
    except KeyError:
        print("GITAPI NOT FOUND")
        os._exit(0)

def debugprint(string):
    print("FileManager: "+string)

def get_version():
    return conf.INFO["version"]

def get_author():
    return conf.INFO["author"]

def autoupdate_isenabled():
    return conf.INFO["autoupdate"]

class explorer:
    def __init__(self):
        pass

    def get_username(self):
        return os.getlogin()

class updateManager:
    def __init__(self, filepath):
        self.main_directory = str(filepath)
        self.split = self.main_directory.split("\\")
        self.main = self.split[len(self.split)-1]

        def is_outdated(self):

            if not get_git_api("name") == get_version():
                return True
            else:   
                return False

        if autoupdate_isenabled() == True:
            debugprint("Latest git release: "+get_git_api("name"))
            debugprint("Installed release: "+get_version())

            if is_outdated(self):
                debugprint("Outdated!")

                mixer.init()
                mixer.music.load(os.path.dirname(os.path.realpath(__file__))+"\Error.mp3")
                mixer.music.set_volume(0.30)
                mixer.music.play(loops=0)

                dialog = messagebox.askyesno(title="OOF", message="New version available ["+get_git_api("name")+"] would you like to download?")
                if dialog == True:

                    url = get_git_api("zipball_url")
                    R = requests.get(url, allow_redirects=True)

                    open(os.path.dirname(os.path.realpath(__file__))+"\\"+self.main[0:len(self.main)-3]+".zip", "wb").write(R.content)

                    with ZipFile(str(os.path.dirname(os.path.realpath(__file__))+"\\"+self.main[0:len(self.main)-3]+".zip"), 'r') as zipObj:
                    # Extract all the contents of zip file in different directory
                        zipObj.extractall(os.path.dirname(os.path.realpath(__file__))+'\\temp')
                        print('File is unzipped in temp folder')

                        self.temp = glob.glob(os.path.dirname(os.path.realpath(__file__))+"\\"+"temp/**/*", recursive=True)   
                        os.system("explorer "+self.temp[0])
                        
            else:
                debugprint("Up to date!")

        else:
            debugprint("Auto-Updating is set to: False, skipping git comparison...")


    