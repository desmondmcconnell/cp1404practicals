from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ("Desmond McConnell", "Terrie-Ann McConnell", "Laek McConnell", "Lune-Fae McConnell")

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.labels_box.add_widget(temp_label)


DynamicLabels().run()
