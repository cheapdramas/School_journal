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
from schedule import Schedule,Item_navig
from login import Login 
from kivymd.uix.boxlayout import BoxLayout
from marks import Marks_screen
from kivymd.uix.bottomnavigation import MDBottomNavigation
from main_navig import Main_navigation






Window.size = (310,580)





class Journal(MDApp):
    
    
    def build(self):
        return Builder.load_file(os.getcwd() + '//kvfiles' + '//total_app.kv')

        # self.sm = MDScreenManager()
        # #DEBUGGING PROCESS CHANGE THE ORDER
        
        # self.sm.add_widget(Login())
        # self.sm.add_widget(Schedule(name ='schedule'))
       
    
       
        # #DEBUGGING PROCESS CHANGE THE ORDER
        
        
    

    



fonts = []
for i in os.listdir(os.getcwd() + '//fonts'):
    fonts.append(os.getcwd() + '//fonts' + f"//{i}")



if __name__ == '__main__':
    for i in fonts:
        LabelBase.register(name = i.split('//')[-1],fn_regular=i)
        

    journal = Journal()
    journal.run()