from kivy.network.urlrequest import UrlRequest
from kivymd.uix.bottomnavigation import MDBottomNavigationItem

from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
import os
from kivymd.uix.scrollview import MDScrollView


class Marks_screen(MDBottomNavigationItem):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        
        
    Builder.load_file(os.getcwd() + '//kvfiles' + '//marks.kv')    
    def make_request(self,user_id):
        
        
        self.r = UrlRequest(f'http://127.0.0.1:5000/get_marks/{user_id}',on_success = self.show)
    def show(self,d,data):
        self.clear_widgets()
        mdscroll = MDScrollView()
        main_box = Main_box()
        all_subjects = ['Алгебра','Англійська мова','Біологія','Географія','Геометрія','Зарубіжна література','Інформатика','Історія України','Мистецтво',"Основи здоров'я",'Правознавство','Трудове навчання','Українська література','Українська мова','Фізика','Фізична культура','Хімія']
        for subj in all_subjects:
            marks_box = Marks_box()
            Mark_label.text = subj
            marks_box.add_widget(Mark_label())
            hor = Horizontal_b()

       

            for subject,mark in data:
                if subject == subj:
                    
                    hor.add_widget(Mark_label(text = str(mark)))
            marks_box.add_widget(hor)
                
                    
            main_box.add_widget(marks_box)
            
                
             

           
            
        
        mdscroll.add_widget(main_box)


        self.add_widget(mdscroll)
            

class Main_box(MDBoxLayout):
    pass

class Marks_box(MDBoxLayout):
    pass
class Horizontal_b(MDBoxLayout):
    pass
class Mark_label(MDLabel):
    pass