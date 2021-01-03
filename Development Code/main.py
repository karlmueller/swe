import kivy
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.clock import Clock
import kivy.properties as kp
from matplotlib import style as mpl_style
from matplotlib import pyplot as plt
from matplotlib import use as mpl_use

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.theming import ThemeManager
from kivy_garden.graph import Graph, MeshLinePlot
from numpy.lib.arraypad import _pad_simple
from client_fx import client_fx
from kivymd.uix.snackbar import Snackbar

Window.size = (9*50, 19.5*50) #remove for builds later... this is OP7P phone ratio right now

nav_widg = '''
#:import Graph kivy_garden.graph.Graph
#:import MeshLinePlot kivy_garden.graph.MeshLinePlot
#:import MeshStemPlot kivy_garden.graph.MeshStemPlot
#:import Snackbar kivymd.uix.snackbar.Snackbar

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
                    text: '192.168.0.161'
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
                    text: '35196'
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

                MDBoxLayout:
                    orientation: 'vertical'

                    MDLabel:
                        id: testYawOut
                        size_hint_y: 0.125
                        size_hint_x: None
                        halign: 'center'

                    MDRectangleFlatButton:
                        id: beginGraphButton
                        text: 'Begin Plotting'
                        pos_hint: {'center_x': 0.25, 'center_y': 0.35}
                        on_release: app.livePlot()

                    MDRectangleFlatButton:
                        id: stopGraphButton
                        text: 'Stop Plotting'
                        pos_hint: {'center_x': 0.75, 'center_y': 0.35}
                        on_release: app.cancelPlot()

                    Graph:
                        id: graph01 
                        title: 'IMU Visualization'
                        xlabel: 'Time'
                        ylabel: 'Angle (deg)'
                        xmin: -10
                        xmax: 0
                        x_ticks_minor: 1
                        x_ticks_major: 5
                        ymin: -180
                        ymax: 180
                        y_ticks_major: 90
                        y_grid_label: True
                        x_grid_label: True
                        padding: 10
                        x_grid: True

            SettingsScreen:
                name: 'settings_screen1'

                MDTextField:
                    id: contact01
                    text: 'muellerkarlw@gmail.com'
                    hint_text: 'Emergency Contact Email'
                    helper_text: 'email of person to be contacted in case of fall'
                    helper_text_mode: 'on_focus'
                    icon_right: 'email'
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint: {'center_x':0.5,'center_y':0.67}
                    size_hint_x: None
                    width: 300

                MDTextField:
                    id: refr_rate_field
                    text: '50'
                    hint_text: 'Refresh rate'
                    helper_text: 'refresh rate of device in Hz'
                    helper_text_mode: 'on_focus'
                    icon_right: 'cellphone-wireless'
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint: {'center_x':0.5,'center_y':0.5}
                    size_hint_x: None
                    width: 300
                    on_text: 
                        Snackbar(text=f'Device refresh rate changed to {refr_rate_field.text} Hz').show()


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
                    color: [1, 1, 1, 1]

                MDLabel:
                    text: 'Fall Detection'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                    color: [1, 1, 1, 1]

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
<VisualizerScreen>:
<SettingsScreen>:
'''
class ConnectionScreen(Screen):
    pass

class VisualizerScreen(Screen):
    pass
    #def build(self):
        #plot_box = BoxLayout()
        #imu_plot = Graph(xlabel='Time', ylabel ='Angle (deg)', x_ticks_minor=0.5,
            #x_ticks_major=2.5, y_ticks_major=180, y_grid_label=True, x_grid_label=True,
            #padding=60, x_grid=True)
        #plot_box.add_widget(imu_plot)
        #return plot_box

class SettingsScreen(Screen):
    pass

#sm = ScreenManager()
#sm.add_widget(ConnectionScreen(name='connection'))
#sm.add_widget(VisualizerScreen(name='visualizer'))
#sm.add_widget(VisualizerScreen(name='setting1'))

# Begin actual coding of the main app class
class sweApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.theme_style = 'Dark'

        mainscreen1 = Builder.load_string(nav_widg)

        self.sensor_refresh = int(mainscreen1.ids.refr_rate_field.text) #handle for this within the imu call and plotting functions

        self.psi = []
        self.phi = []
        self.theta = []


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

        try:
            self.imu_instance = client_fx(ip_input, port_input)
            Snackbar(text=f'Attempting connection with {ip_input} : {port_input}').show()
        except: 
            Snackbar(text=f'Cannot connect with {ip_input} : {port_input}... try again later').show()

    def updatePoints(self, *args):
        instant_imu = self.imu_instance.dq.get()
        self.c_time = instant_imu[0] - 1609477200 #epoch time since beg 2021

        if len(self.psi) > 1000:
            self.psi.append([self.c_time, instant_imu[1]])
            self.phi.append([self.c_time, instant_imu[2]])
            self.theta.append([self.c_time, instant_imu[3]])

            self.psi = self.psi[-1:-7*self.sensor_refresh]
            self.phi = self.phi[-1:-7*self.sensor_refresh]
            self.theta = self.theta[-1:-7*self.sensor_refresh]

        else:
            self.psi.append([self.c_time, instant_imu[1]])
            self.phi.append([self.c_time, instant_imu[2]])
            self.theta.append([self.c_time, instant_imu[3]])

        plot_psi = MeshLinePlot(color=[1, 0, 0, 1])
        plot_phi = MeshLinePlot(color=[0, 1, 0, 1])
        plot_theta = MeshLinePlot(color=[0, 0, 1, 1])

        plot_psi.points = self.psi
        plot_phi.points = self.phi
        plot_theta.points = self.theta

        self.root.ids.graph01.add_plot(plot_psi)
        self.root.ids.graph01.add_plot(plot_phi)
        self.root.ids.graph01.add_plot(plot_theta)

        self.root.ids.testYawOut.text = f'{instant_imu[1]}-> yaw'
        #print(f'{instant_imu[0]}')


    def updateAxis(self, *args):
        new_time_min = self.c_time - 10  #define an epoch time in seconds that is 10 seconds in the past

        self.root.ids.graph01.xmin = round(new_time_min)
        self.root.ids.graph01.xmax = round(self.c_time)

    def livePlot(self, *args):
        self.graph_activate = True
        Clock.schedule_interval(self.updatePoints, 1/self.sensor_refresh)
        Clock.schedule_interval(self.updateAxis, 1/self.sensor_refresh)

    def cancelPlot(self, *args):
        Clock.unschedule(self.updatePoints)
        Clock.unschedule(self.updateAxis)


if __name__ == '__main__':
    sweApp().run()
