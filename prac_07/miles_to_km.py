from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class MilesToKilometresConverter(App):

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_increment(self, value, miles_input):
        result = self.get_valid_miles(miles_input.text) + value
        if result < 0:
            result = 0.0
        miles_input.text = "{}".format(result)

    def handle_conversion(self, miles_input, display_label):
        value = self.get_valid_miles(miles_input.text)
        kilometres = value * MILES_TO_KM
        display_label.text = str(kilometres)

    def get_valid_miles(self, miles_input):
        try:
            value = float(miles_input)
            return value
        except ValueError:
            return 0


MilesToKilometresConverter().run()
