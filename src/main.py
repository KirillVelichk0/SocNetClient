from KinterBase import root_gui
from RegAuthMenu import RegAuthMenu

if __name__ == '__main__':

    gui = [RegAuthMenu()]
    gui[0].CreateMenu(gui)
    root_gui.mainloop() 
