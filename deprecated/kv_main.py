#Code basics and learnings from Sentdex App tutorital
#https://www.youtube.com/watch?v=FjwD0SOGQ1k&list=PLQVvvaa0QuDfwnDTZWw8H3hN_VRQfq8rF
#Karl Mueller --> 12/12/2020


import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

import os


class ConnectPage(GridLayout): #Input page for IP, port, other info, connect button

    def __init__(self, **kwargs): #will run the gridlayout method
        super().__init__(self)
        self.cols = 2
  
        if os.path.isfile('config.text'): #handle for previously input config
            with open('config.txt','r') as f:
                details = f.read().split(',')
                config_ip = details[0]
                config_port = details[1]
        else:
            config_ip = ''
            config_port = ''

        #Generate label and input field for IP ADDR
        self.add_widget(Label(text='IP Address:'))

        self.ip = TextInput(text=config_ip, multiline=False)
        self.add_widget(self.ip)

        #Generate label and input field for port number
        self.add_widget(Label(text='Port No.:'))

        self.port = TextInput(text=config_port, multiline=False)
        self.add_widget(self.port)

        #Generate button to ocnnect to server
        self.connect = Button(text='Connect')
        self.connect.bind(on_press=self.connect_button)
        self.add_widget(Label())
        self.add_widget(self.connect)

    def connect_button(self, instance):
        ip = self.ip.text
        port = self.port.text

        print(f'Attempting to connect to {ip}:{port} detection unit')

        with open('config.txt', 'w') as f:
            f.write(f'{ip},{port}')


class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.cols = 1
        self.message = Label(halign='center', valign='middle', font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

    def update_into(self, message):
        self.message.text = message

    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*0.9, None)




class FallApp(App):
    def build(self): #intitialization method

        #Screen manager init
        self.screen_manager = ScreenManager()

        #Connection page for internet connection
        self.connect_page = ConnectPage()
        screen = Screen(name='Connect')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name='Info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager





if __name__ == "__main__":
    swe = FallApp()
    swe.run()