import kivy
from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton

from client_fx import client_fx #custom client code import function/object class

Window.size = (9*50, 19.5*50) #remove for builds later... this is OP7P phone ratio right now

screen_helper = '''
Screen: 
    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: 'Swe Application PRE_BETA'
            left_action_items: [['menu',lambda x: app.navigation_draw()]]
            elevation: 9
        MDLabel:
            text: ''

'''

class sweApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.theme_style = 'Dark'
        screen1 = Builder.load_string(screen_helper)

        self.ip_addr = Builder.load_file('ip_helper.kv')

        self.conn_button = MDRectangleFlatButton(text='WLan Connect',
            pos_hint= {'center_x': 0.5, 'center_y': 0.15},
            on_release=self.connect_to_imu
            )



        screen1.add_widget(self.ip_addr)
        screen1.add_widget(self.conn_button)

        return screen1

    def connect_to_imu(self, obj):
        
        if self.ip_addr.text is "":
            handle_ip_empty = "Please enter the Swe IP address"
        else:
            pass

        self.imu = client_fx() # creates imu connection instance and code runs in background thread
        close_button = MDFlatButton(text='Ja', on_release=self.close_dialog)

        self.dialog = MDDialog(title='Connecting...', text='Connection with Swe Initializing...',
            size_hint=(0.7, 1),
            buttons=[close_button])

        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()

    def navigation_draw(self):
        print('navigation')

        

if __name__ == '__main__':
    sweApp().run()
