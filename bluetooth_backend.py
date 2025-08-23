import threading
import time
class BluetoothManager:
    def __init__(self):
        self.devices = []
        self.callback = None
        self.running = False
    def start_scan(self, callback):
        self.callback = callback
        self.running = True
        threading.Thread(target=self.scan_loop, daemon=True).start()
    def scan_loop(self):
        while self.running:
            time.sleep(15)
            if self.callback:
                self.callback("msg_chiffre", "Utilisateur1")
    def send(self, encrypted_text):
        pass