import kivy
kivy.require('2.0.0') # kivy_venv\Scripts\activate

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class PWM(App):

    def build(self):
        return Label(text='Hello world')


class AuthPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

if __name__ == '__main__':
    PWM().run()