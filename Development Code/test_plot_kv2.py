from math import sin, cos

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout

from kivy.garden.graph import Graph, MeshLinePlot


class Plot(RelativeLayout):
    def __init__(self, **kwargs):
        super(Plot, self).__init__(**kwargs)
        self.graph = Graph(xlabel="x", ylabel="y", x_ticks_minor=5, x_ticks_major=25, y_ticks_major=1,
                           y_grid_label=True, x_grid_label=True, x_grid=True, y_grid=True,
                           xmin=-0, xmax=100, ymin=-1, ymax=1, draw_border=False)
        # graph.size = (1200, 400)
        # self.graph.pos = self.center

        self.plot = MeshLinePlot(color=[1, 1, 1, 1])
        self.plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        self.plot2 = MeshLinePlot(color=[1, 0, 0, 1])
        self.plot2.points = [(x, cos(x / 10.)) for x in range(0, 101)]
        self.add_widget(self.graph)

        self.graph.add_plot(self.plot)
        self.graph.add_plot(self.plot2)


class GraphLayoutApp(App):

    def build(self):
        scroll_view = ScrollView()
        grid_layout = GridLayout(cols=1, padding=20, spacing=20, size_hint_y=None)
        grid_layout.bind(minimum_size=grid_layout.setter('size'))
        graph = Plot(size_hint_y=None, height=500)
        graph2 = Plot(size_hint_y=None, height=500)
        label = Label(text="Hello World!", size_hint_y=None)
        label2 = Label(text="Hello World!", size_hint_y=None)
        grid_layout.add_widget(label)
        grid_layout.add_widget(graph)
        grid_layout.add_widget(label2)
        grid_layout.add_widget(graph2)
        scroll_view.add_widget(grid_layout)

        # return grid_layout
        return scroll_view

if __name__ == '__main__':
    GraphLayoutApp().run()
