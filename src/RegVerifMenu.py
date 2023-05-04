from MenuBase import BaseMenu as Base
from tkinter import Button as TkButton, Entry as TkEntry, Label as TkLabel
from tkinter import messagebox

class RegVerifMenu(Base):
    
    def __verify(self):
        ...

    def __init__(self):
        ...

    def __set_sizes_and_poses(self):
        self.__token_label.place(height=100, width= 300, x= 350, y=10)
        self.__token_entry.place(height=100, width= 300, x= 350, y=200)
        self.__token_button.place(height=100, width= 300, x= 350, y=370)
        ...

    def CreateMenu(self, instanse):
        self.__token_label = TkLabel(text='Введите код потдверждения')
        self.__token_entry = TkEntry()
        self.__token_button = TkButton(text='Подтверждение',\
                                        command=self.__verify)
        self.__set_sizes_and_poses()
        self.__instanse = instanse

    def DestroyMenu(self, instanse):
        ...