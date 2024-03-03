from kivy.network.urlrequest import UrlRequest
from kivymd.uix.bottomnavigation import MDBottomNavigationItem

from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
import os
from kivymd.uix.scrollview import MDScrollView
from datetime import *
from kivy.uix.button import Button



class News(MDBottomNavigationItem):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.id_user = 0
        self.data = 0
        

    Builder.load_file(os.getcwd() + '//kvfiles' + '//news.kv')


    def make_request(self,user_id):
        self.id_user = user_id
        UrlRequest(f'http://127.0.0.1:5000/get_news/{user_id}',on_success = self.show)

    def show(self,d,data):
        self.data = data
        self.clear_widgets()
        
        
        scroll = MDScrollView()
        #main_box = Main_box_()
        current_time = date.today()
        
        yesterday= current_time- timedelta(1)

        list_when = []
        data.reverse()


        

        for i in data:
            if datetime.strptime(i[3], '%Y-%m-%d') == datetime.strptime(str(current_time), '%Y-%m-%d'):
                i[3] = 'Сьогодні'
            elif datetime.strptime(i[3], '%Y-%m-%d') == datetime.strptime(str(yesterday), '%Y-%m-%d'):
                i[3] = 'Вчора'
            else:
                curr = datetime.strptime(str(current_time), '%Y-%m-%d') 
                datas_time = datetime.strptime(i[3], '%Y-%m-%d')
                delta = curr - datas_time
                i[3] = str(delta.days) +'д тому'

        grid = GridLayout(cols=1,spacing = 10,size_hint_y = None)
        grid.bind(minimum_height=grid.setter('height'))
        

        for i in data:
            
            n = MDBoxLayout(orientation = 'vertical',spacing = 10,size_hint_y = None,md_bg_color=(0, 1, 1, 1))
            n.add_widget(MDLabel(text = f'Нова оцінка з предмету:{i[0]},{i[1]},{i[2]}',size_hint_y=None,height =100,halign = 'left'))
            n.add_widget(MDLabel(text = f'{i[3]},{i[4]}',size_hint_y=None,height =1,halign = 'right'))
            grid.add_widget(n)

        scroll.add_widget(grid)

        self.add_widget(scroll)
        
    def update_on_press(self):
        self.clear_widgets()
        self.make_request(self.id_user)
        


        
        

       
        

            



        
            



        

