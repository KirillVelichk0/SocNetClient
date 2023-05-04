from tkinter import Tk

class App(Tk):
    def __init__(self, loop, interval):
        super().__init__()
        self.loop = loop
        self.interval = interval

root_gui = Tk()
root_gui.geometry('1000x500')
root_gui.title('SocNetClient')

