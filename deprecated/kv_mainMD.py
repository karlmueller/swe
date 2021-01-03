#Code basics and learnings from Sentdex App tutorital
#https://www.youtube.com/watch?v=FjwD0SOGQ1k&list=PLQVvvaa0QuDfwnDTZWw8H3hN_VRQfq8rF
#Karl Mueller --> 12/12/2020

build_no = '0.100a'  # build number for reference
import kivy
kivy.require('2.0.0')

from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemableBehavior, ThemeManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.font_definitions import theme_font_styles
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from client_fx import client_fx
from kivy.properties import ObjectProperty


#from kivy.garden.matplotlib.backend_kivy import FigureCanvasKivy


'''
class ConnectPage(Screen):
    def __init__(self, **kwargs):
        super(ConnectPage, self).__init__(**kwargs)

        self.ip_field = MDTextField(hint_text='Enter IP Address',
                                    helper_text='IP address of Swe product',
                                    helper_text_mode='on_focus',
                                    icon_right='cellphone-wireless',
                                    pos_hint= {'center_x': 0.5, 'center_y': 0.6},
                                    size_hint_x= None,
                                    width= 300)

        self.port_field = MDTextField(hint_text='Enter Port',
                                    helper_text='Port Number of Swe product',
                                    helper_text_mode='on_focus',
                                    icon_right='power-plug',
                                    pos_hint={'center_x': 0.5,'center_y': 0.45},
                                    size_hint_x=None,
                                    width=300)

        self.connect_button = MDRectangleFlatButton(
                                    text='Connect to Swe',
                                    pos_hint={'center_x': 0.5, 'center_y': 0.1})

        self.add_widget(self.ip_field)
        self.add_widget(self.port_field)
        self.add_widget(self.connect_button)


class OptionsPage(Screen):
    def __init__(self, **kwargs):
        super(OptionsPage, self).__init__(**kwargs)

        self.email_field = MDTextField(hint_text='Enter email address',
                                    helper_text='Email address of emergency contact',
                                    helper_text_mode='on_focus',
                                    icon_right='cellphone-wireless',
                                    pos_hint={'center_x': 0.5,'center_y': 0.6},
                                    size_hint_x=None,
                                    width=300)


        self.add_widget(self.email_field)
'''

class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '200'
        self.theme_cls.theme_style = 'Dark'

        s = Screen()

        lower_bar_nav = Builder.load_file('bottomnav.kv')
        
        s.add_widget(lower_bar_nav)
        connectButton.bind()
        return s

    #def rpi_connect(self, **kwargs):

if __name__=='__main__':
    MainApp().run()
