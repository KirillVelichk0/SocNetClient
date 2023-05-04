from MenuBase import BaseMenu as Base
from tkinter import Button as TkButton, Entry as TkEntry, Label as TkLabel
from tkinter import messagebox
import requests, ConfigParser
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class RegMenu(Base):

    def __init__(self):
        config = ConfigParser.ParseMicrConfig()
        self.__con_str = config['Soc_net_aut_proxy']

    def __set_pos_sz(self):
        self.__email_label.place(height=70, width= 300, x= 350, y=10)
        self.__email_entry.place(height=70, width= 300, x= 350, y=100)
        self.__pass_label.place(height=70, width= 300, x= 350, y=200)
        self.__pass_entry.place(height=70, width= 300, x= 350, y=290)
        self.__reg_button.place(height=70, width= 300, x= 350, y=400)

    def __regitstrate_event(self):
        email = self.__email_entry.get()
        password = self.__pass_entry.get()
        if email == '' or password == '':
            messagebox.showinfo('Нет данных','Пожалуйста, введите учетные данные')
            return
        url = 'https://' + self.__con_str + '/registration'
        r = requests.post(url=url, json={'email': email, 'password': password},\
                            verify=False,\
                            headers={ "Accept": "application/json", "Content-Type": "application/json" })
        json_answer = r.json()
        if r.status_code == 200:
            messagebox.showinfo(title='reg_result', message=json_answer['result'])
        elif r.status_code == 401:
            messagebox.showwarning(title='reg_result', message='401 error\n' + json_answer['error'])
        else:
            messagebox.showwarning(title='reg_result', message='Some problems')


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

