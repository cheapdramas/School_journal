from kivy.lang import Builder
import os
from kivymd.uix.screen import MDScreen
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.bottomnavigation import MDBottomNavigation,MDBottomNavigationItem




class Schedule(MDScreen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


class Item_navig(MDBottomNavigationItem):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
        UrlRequest('http://127.0.0.1:5000/schedule',on_success =self.display_info)
        Builder.load_file(os.getcwd() + '//kvfiles' + '//schedule.kv')

    def display_info(self,a,b):
        mdscroll = MDScrollView()
        

        box = Box_main()

        for sch in b:
            box_sched = Box_sched()
            for item in sch:
                if item != None:
                    print(item)
                    if sch.index(item) == 0:
                        box_sched.add_widget(MDLabel(text = f'{item}',color = (0,0,0,1),halign= 'left'))
                    else:
                        box_sched.add_widget(MDLabel(text = f'{sch.index(item)}.{item}',color = (0,0,0,1),halign= 'center'))
            box.add_widget(box_sched)
        
       

        mdscroll.add_widget(box)
        
        
        self.add_widget(mdscroll)


class Box_main(MDBoxLayout):    
    pass
    

class Box_sched(MDBoxLayout):
    pass
