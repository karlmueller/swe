import numpy as np
import matplotlib.widgets as widgets
import PIL
import matplotlib as mpl
from matplotlib import pyplot as plt
from PIL import Image
from kivy.app import App
from kivy.lang import Builder
from kivy_matplotlib import MatplotFigure, MatplotNavToolbar
from kivy.uix.screenmanager import ScreenManager, Screen

kv = """
<ScreenTwo>:
    id:sc1
    BoxLayout:
        FileChooserListView:
            id: filechooser
            on_selection: my_widget.selected(filechooser.selection)
        Button:
            text: "Go to Screen 1"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_one'

<ScreenOne>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:"Choose File"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_two'
        MatplotFigure:
            id: figure_wgt
            size_hint: 1, 0.9
        MatplotNavToolbar:
            id: navbar_wgt
            size_hint: 1, 0.1
            figure_widget: figure_wgt
"""
# Insert string into Language builder.
Builder.load_string(kv)


class ScreenOne(Screen):
    pass


class ScreenTwo(Screen):
    pass


# The ScreenManager controls moving between screens
screen_manager = ScreenManager()
screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))


class testApp(App):
    title = "Test Matplotlib"

    def build(self):

        # ....

        # get first screen and update figure

        screen_one = screen_manager.get_screen('screen_one')

        screen_one.ids['figure_wgt'].figure = fig

        return screen_manager


sample_app = testApp()
sample_app.run()
