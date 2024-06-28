from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = MDLabel(
            text="Bem-vindo ao SmartEntrega!",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 0, 0, 1)  # Vermelho
        )
        self.add_widget(label)

class MainApp(MDApp):
    def build(self):
        screen = MainScreen(name='main')
        return screen

if __name__ == '__main__':
    MainApp().run()