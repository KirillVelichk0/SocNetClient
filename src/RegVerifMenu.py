from MenuBase import BaseMenu as Base
from tkinter import Button as TkButton, Entry as TkEntry, Label as TkLabel
from tkinter import messagebox
from ConfigParser import ParseMicrConfig
import requests
from FormLoader import LoadNextForm

class RegVerifMenu(Base):
    
    def __load_reg_auth_form(self):
        from RegAuthMenu import RegAuthMenu as RAMenu
        self.__instanse = LoadNextForm(RAMenu(), self.__instanse)
        ...

    def __verify(self):
        token = self.__token_entry.get()
        if token == '':
            messagebox.showinfo('Нет данных','Пожалуйста, введите учетные данные')
            return
        url = 'https://' + self.__con_str + '/registration_verification'
        try:
            r = requests.post(url=url, json={'random_data_token': token},\
                                verify=False,\
                                headers={ "Accept": "application/json", "Content-Type": "application/json" })
            json_answer = r.json()
            if r.status_code == 200:
                messagebox.showinfo(title='reg_result', message=json_answer['response_message'])
                self.__load_reg_auth_form()
            elif r.status_code == 401:
                messagebox.showwarning(title='reg_result', message='401 error\n' + json_answer['error'])
            else:
                messagebox.showwarning(title='reg_result', message='Some problems')
        except:
            messagebox.showwarning(title='Упс...', message='Что-то пошло не так')
        ...

    def __init__(self):
        config = ParseMicrConfig()
        self.__con_str = config['Soc_net_aut_proxy']
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
        self.__token_button.destroy()
        self.__token_entry.destroy()
        self.__token_label.destroy()