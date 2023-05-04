from MenuBase import BaseMenu as Base
from tkinter import Button as TkButton
from RegMenu import RegMenu


class RegAuthMenu(Base):
    def __registrate_event(self):
        next_instanse = RegMenu()
        self.DestroyMenu(self.__instanse)
        self.__instanse[0] = next_instanse
        self.__instanse[0].CreateMenu(self.__instanse)
        self.__instanse = None

    def __login_event(self):
        ...

    def __init__(self):
        ...

    def CreateMenu(self, instanse):
        self.__reg_button = TkButton(text= 'Регистрация',command= self.__registrate_event)
        self.__login_button = TkButton(text= 'Войти', command= self.__login_event)
        self.__reg_button.place(height=150, width= 300, x= 350, y=70)
        self.__login_button.place(height=150, width= 300, x= 350, y=240)
        self.__instanse = instanse

    def DestroyMenu(self, instanse):
        self.__reg_button.destroy()
        self.__login_button.destroy()