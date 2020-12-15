import kivy
from kivy.lang import Builder
from kivy.core.window import Window


from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.theming import ThemeManager
from client_fx import client_fx

from kivy.garden.graph import 

Window.size = (9*50, 19.5*50) #remove for builds later... this is OP7P phone ratio right now

nav_widg = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Swe: Build 0.01a'
            left_action_items: [['menu', lambda x: nav_drawer1.toggle_nav_drawer()]]
            elevation: 10
        Widget:
            title: ''
    NavigationLayout:
        ScreenManager:
            id: screen_mgr1

            ConnectionScreen:
                name: 'connection_screen1'

                MDTextField:
                    id: ipAddr
                    hint_text: 'Enter IP Address'
                    helper_text: 'IP Address of Swe Product'
                    helper_text_mode: 'on_focus'
                    icon_right: 'cellphone-wireless'
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint: {'center_x':0.5,'center_y':0.67}
                    size_hint_x: None
                    width: 300

                MDTextField:
                    id: portAddr
                    hint_text: 'Enter Port'
                    helper_text: 'Port number of Swe product'
                    helper_text_mode: 'on_focus'
                    icon_right: 'power-plug'
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                    size_hint_x: None
                    width: 300

                MDRectangleFlatButton:
                    id: connectButton
                    text: 'Connect to Swe'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                    on_release: app.call_imu_data()

            VisualizerScreen:
                name: 'visualizer_screen1'
                MDLabel:
                    text: 'Visualizer Placeholder'

            SettingsScreen:
                name: 'settings_screen1'
                MDLabel:
                    text: 'Settings Placeholder'

        MDNavigationDrawer:
            id: nav_drawer1

            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'swe_logo.png'

                MDLabel:
                    text: 'Swe Technologies'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: 'Fall Detection'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Connectivity'
                            on_release: screen_mgr1.current ='connection_screen1'
                            IconLeftWidget:
                                icon: 'access-point'
                        OneLineIconListItem:
                            text: 'Posture Visualizer'
                            on_release: screen_mgr1.current = 'visualizer_screen1'
                            IconLeftWidget: 
                                icon: 'axis-arrow'
                        OneLineIconListItem:
                            text: 'Settings'
                            on_release: screen_mgr1.current = 'settings_screen1'
                            IconLeftWidget:
                                icon: 'cogs'

<ConnectionScreen>:
    name: 'connection'
<VisualizerScreen>:
    name: 'visualizer'
    MDLabel: 
        text: 'Visualization Screen'
        halign: 'center'
<SettingsScreen>:
    name: 'setting1'
    MDLabel: 
        text: 'Settings Screen'
        halign: 'center'

'''

class ConnectionScreen(Screen):
    pass

class VisualizerScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(ConnectionScreen(name='connection'))
sm.add_widget(VisualizerScreen(name='visualizer'))
sm.add_widget(VisualizerScreen(name='setting1'))

class sweApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.theme_style = 'Dark'


        mainscreen1 = Builder.load_string(nav_widg)



        return mainscreen1

    def connect_to_imu(self, obj):
        
        if self.root.ids.ipAddr.text is "":
            handle_ip_empty = "Please enter the Swe IP address"
        else:
            pass


        #self.imu = client_fx() # creates imu connection instance and code runs in background thread
        close_button = MDFlatButton(text='Ja', on_release=self.close_dialog)

        self.dialog = MDDialog(title='Connecting...', text='Connection with Swe Initializing...',
            size_hint=(0.7, 1),
            buttons=[close_button])

        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()

    def navigation_draw(self):
        print('navigation')

    def call_imu_data(self):
        ip_input = self.root.ids.ipAddr.text
        port_input = int(self.root.ids.portAddr.text)

        self.imu_instance = client_fx(ip_input, port_input)



    def print_imu(self):
        
        plot = MeshLinePlot(color=next(colors))

        


        

if __name__ == '__main__':
    sweApp().run()
