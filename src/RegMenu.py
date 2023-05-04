from MenuBase import BaseMenu as Base
from tkinter import Button as TkButton, Entry as TkEntry, Label as TkLabel


class RegMenu(Base):

    def __set_pos_sz(self):
        self.__email_label.place(height=70, width= 300, x= 350, y=10)
        self.__email_entry.place(height=70, width= 300, x= 350, y=100)
        self.__pass_label.place(height=70, width= 300, x= 350, y=200)
        self.__pass_entry.place(height=70, width= 300, x= 350, y=290)
        self.__reg_button.place(height=70, width= 300, x= 350, y=400)

    def __regitstrate_event(self):
        ...

    def CreateMenu(self, instanse):
        self.__email_label = TkLabel(text='Введите почту')
        self.__email_entry = TkEntry()
        self.__pass_label = TkLabel(text = 'Введите пароль')
        self.__pass_entry = TkEntry()
        self.__reg_button = TkButton(text='Регистрация', command=self.__regitstrate_event)
        self.__set_pos_sz()
        self.__instanse = instanse

    def DestroyMenu(self, instanse):
        pass

