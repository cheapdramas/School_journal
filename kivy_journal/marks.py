from kivymd.uix.screen import MDScreen
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from user import User
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
import os
from kivymd.uix.scrollview import MDScrollView


class Marks_screen(MDBottomNavigationItem):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.user_id = 0
        
        
    Builder.load_file(os.getcwd() + '//kvfiles' + '//marks.kv')    
    def make_request(self,user_id):
        
        self.r = UrlRequest(f'http://127.0.0.1:5000/get_marks/{user_id}',on_success = self.show)
        
    def show(self,d,data):
        print(data)
        mdscroll = MDScrollView()
        main_box = Main_box()
        all_subjects = ['Алгебра','Англійська','Біологія','Географія','Геометрія','Зарубіжна література','Іноземна мова(англ)','Інформатика','Історія України','Мистецтво',"Основи здоров'я",'Правознавство','Трудове навчання','Українська література','Українська мова','Фізика','Фізична культура','Хімія']
        for i in all_subjects:
            subj_box = Subj_box()
            subj_box.add_widget(MDLabel(text = i))
            for tuple in data:
                if tuple[0] == i:
                    subj_box.add_widget(MDLabel(text = str(tuple[1])))

            main_box.add_widget(subj_box)
        mdscroll.add_widget(main_box)


        self.add_widget(mdscroll)
            

class Main_box(MDBoxLayout):
    pass

class Subj_box(MDBoxLayout):
    pass