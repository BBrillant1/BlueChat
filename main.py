from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from bluetooth_backend import BluetoothManager
from database import Database
from crypto import encrypt_message, decrypt_message

class ChatUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.db = Database("chat_db.sqlite")
        self.bt_manager = BluetoothManager()
        self.chat_area = GridLayout(cols=1, size_hint_y=None)
        self.chat_area.bind(minimum_height=self.chat_area.setter('height'))
        scroll = ScrollView(size_hint=(1, 0.85))
        scroll.add_widget(self.chat_area)
        self.add_widget(scroll)
        input_box = BoxLayout(size_hint_y=0.15)
        self.input_text = TextInput(multiline=False)
        send_btn = Button(text="Envoyer")
        send_btn.bind(on_release=self.send_message)
        input_box.add_widget(self.input_text)
        input_box.add_widget(send_btn)
        self.add_widget(input_box)
        self.bt_manager.start_scan(callback=self.receive_message)
    def send_message(self, instance):
        text = self.input_text.text
        if not text.strip():
            return
        encrypted = encrypt_message(text)
        self.bt_manager.send(encrypted)
        self.db.save_message("me", text)
        self.display_message("me", text)
        self.input_text.text = ""
    def receive_message(self, encrypted_text, sender):
        text = decrypt_message(encrypted_text)
        self.db.save_message(sender, text)
        self.display_message(sender, text)
    def display_message(self, sender, text):
        label = Label(text=f"[b]{sender}:[/b] {text}", markup=True, size_hint_y=None)
        label.bind(texture_size=label.setter('size'))
        self.chat_area.add_widget(label)

class ChatApp(App):
    def build(self):
        return ChatUI()

if __name__ == "__main__":
    ChatApp().run()