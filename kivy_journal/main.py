from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.core.window import Window
import os
import sqlite3
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.screen import MDScreen
from kivymd.uix.widget import MDWidget
from schedule import Schedule
from login import Login
from kivymd.uix.boxlayout import BoxLayout



Window.size = (310,580)


class Main_layout(BoxLayout):
    pass


class Journal(MDApp):
    
    
    def build(self):
        
        self.sm = MDScreenManager()
        #DEBUGGING PROCESS CHANGE THE ORDER
        
        self.sm.add_widget(Login())
        self.sm.add_widget(Schedule(name = 'schedule'))
        
        
        
       
        #DEBUGGING PROCESS CHANGE THE ORDER
        
        
        return self.sm



fonts = []
for i in os.listdir(os.getcwd() + '//fonts'):
    fonts.append(os.getcwd() + '//fonts' + f"//{i}")



if __name__ == '__main__':
    for i in fonts:
        LabelBase.register(name = i.split('//')[-1],fn_regular=i)
        

    journal = Journal()
    journal.run()