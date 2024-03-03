from kivy.lang import Builder
from kivy.core.window import Window
import os
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton

from marks import Marks_screen
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from main_navig import Main_navigation
from news import News

class Login(MDScreen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        

    Builder.load_file(os.getcwd() + '//kvfiles' + "//login.kv")
    def login_legitcheck(self):
        self.login_input =self.ids.login_input.text
        self.password_input = self.ids.password.text
        request = UrlRequest('http://127.0.0.1:5000/students_log',on_success=self.success_log)
        

    def success_log(self,daemon,data_for_log):
        #data = [[1,login,password],[2,login,password]]
        
        for list_info in data_for_log:
            
            
            if self.login_input == list_info[1] and self.password_input == list_info[2]:

                m = Marks_screen()
                n = News()
                m.make_request(list_info[0])
                n.make_request(list_info[0])
                
                
                self.manager.ids.navigation.add_widget(m)
                self.manager.ids.navigation.add_widget(n)
                self.retranslate_to_schedule_if_success(True)
                
                
                
                

    def retranslate_to_schedule_if_success(self,retranslate):
        if retranslate:
            
            self.manager.current = 'schedule'
            
            

            #Marks_screen().id = user.id

