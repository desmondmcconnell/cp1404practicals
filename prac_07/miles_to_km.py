from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesToKilometresConverter(App):

    def build(self):
        """ build the Kivy app from the kv file """
        # Window.size = (300, 150)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_increment(self, value, miles_input):
        finished = False
        while not finished:
            try:
                result = float(miles_input.text) + value
                finished = True
            except(ValueError):
                miles_input.text = "0.0"
        if result < 0:
            result = 0.0
        miles_input.text = "{}".format(result)

    def handle_conversion(self, miles_input, display_label):
        finished = False
        while not finished:
            try:
                kilometres = float(miles_input.text) * MILES_TO_KM
                finished = True
            except(ValueError):
                miles_input.text = "0.0"
        # kilometres = str(float(miles_input.text) * 1.60934)
        display_label.text = "{:.5}".format(kilometres)


MilesToKilometresConverter().run()
