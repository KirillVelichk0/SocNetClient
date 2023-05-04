from KinterBase import root_gui
from RegAuthMenu import RegAuthMenu
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if __name__ == '__main__':

    gui = [RegAuthMenu()]
    gui[0].CreateMenu(gui)
    root_gui.mainloop() 
