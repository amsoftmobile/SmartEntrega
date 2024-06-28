from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username_field = MDTextField(
            hint_text="Nome de Usuário",
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            size_hint_x=None,
            width=Window.width * 0.8
        )
        self.add_widget(self.username_field)

        self.password_field = MDTextField(
            hint_text="Senha",
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint_x=None,
            width=Window.width * 0.8,
            password=True  # Mostra asteriscos
        )
        self.add_widget(self.password_field)

        self.login_button = MDRaisedButton(
            text="Entrar",
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            size_hint_x=None,
            width=Window.width * 0.8,
            on_press=self.login
        )
        self.add_widget(self.login_button)

    def login(self, instance):
        # Aqui você colocaria a lógica para validar o login
        username = self.username_field.text
        password = self.password_field.text
        print(f"Usuário: {username}, Senha: {password}")