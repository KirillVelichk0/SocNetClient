from MenuBase import BaseMenu as Base
from tkinter import Button as TkButton, Entry as TkEntry, Label as TkLabel
from tkinter import messagebox
import requests, ConfigParser
from FormLoader import LoadNextForm
from DBMaster import master as db_master

class LoginMenu(Base):

    def __init__(self):
        config = ConfigParser.ParseMicrConfig()
        self.__con_str = config['Soc_net_aut_proxy']

    def __set_pos_sz(self):
        self.__email_label.place(height=70, width= 300, x= 350, y=10)
        self.__email_entry.place(height=70, width= 300, x= 350, y=100)
        self.__pass_label.place(height=70, width= 300, x= 350, y=200)
        self.__pass_entry.place(height=70, width= 300, x= 350, y=290)
        self.__log_button.place(height=70, width= 300, x= 350, y=400)


    '''def __load_verify_form(self):
        import RegVerifMenu
        self.__instanse = LoadNextForm(RegVerifMenu.RegVerifMenu(), self.__instanse)'''

    def __login_event(self):
        email = self.__email_entry.get()
        password = self.__pass_entry.get()
        if email == '' or password == '':
            messagebox.showinfo('Нет данных','Пожалуйста, введите учетные данные')
            return
        url = 'https://' + self.__con_str + '/login'
        try:
            r = requests.post(url=url, json={'email': email, 'password': password},\
                                verify=False,\
                                headers={ "Accept": "application/json", "Content-Type": "application/json" })
            json_answer = r.json()
            if r.status_code == 200:
                messagebox.showinfo(title='login_result', message=json_answer['result'])
                if bool(json_answer['user_id'] != -1):
                    db_master.UpdateJWT(json_answer['jwtToken'])
                    #добавить сохранение токена, а также переход в другую форму
                    ...
            elif r.status_code == 401:
                messagebox.showwarning(title='login_result', message='401 error\n' + json_answer['error'])
            else:
                messagebox.showwarning(title='login_result', message='Some problems')
        except:
            messagebox.showwarning(title='Упс...', message='Что-то пошло не так')



    def CreateMenu(self, instanse):
        self.__email_label = TkLabel(text='Введите почту')
        self.__email_entry = TkEntry()
        self.__pass_label = TkLabel(text = 'Введите пароль')
        self.__pass_entry = TkEntry()
        self.__log_button = TkButton(text='Вход', command=self.__login_event)
        self.__set_pos_sz()
        self.__instanse = instanse

    def DestroyMenu(self, instanse):
        self.__email_label.destroy()
        self.__email_entry.destroy()
        self.__pass_label.destroy()
        self.__pass_entry.destroy()
        self.__log_button.destroy()

