from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import MDLabel
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from screens.main_screen import MainScreen

class SmartEntregaApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    SmartEntregaApp().run()