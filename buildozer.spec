[app]
title = Bluetooth Chat Pro
package.name = bluetoothchatpro
package.domain = org.example
source.include_exts = py,png,jpg,kv
source.dir = .
version = 1.0
requirements = python3,kivy,pyjnius,cryptography,plyer
orientation = portrait
android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,ACCESS_FINE_LOCATION,INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,RECORD_AUDIO
icon.filename = assets/avatar.png
log_level = 2
warn_on_root = 1
android.release = 1
android.archs = arm64-v8a

# Ajoute cette ligne en dehors de la section [app], à la fin du fichier :
android.sdk_path = $HOME/.buildozer/android/platform/android-sdk