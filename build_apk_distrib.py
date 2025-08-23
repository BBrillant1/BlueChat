import os
import shutil
import subprocess
PROJECT_DIR = os.path.abspath(".")
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")
ASSETS_SOURCE_DIR = os.path.join(PROJECT_DIR, "assets_source")
REQUIRED_FILES = ["main.py","bluetooth_backend.py","database.py","crypto.py","buildozer.spec"]
APK_OUTPUT_DIR = os.path.join(PROJECT_DIR,"bin")
def ensure_assets():
    if not os.path.isdir(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)
    if os.path.isdir(ASSETS_SOURCE_DIR):
        for f in os.listdir(ASSETS_SOURCE_DIR):
            src = os.path.join(ASSETS_SOURCE_DIR,f)
            dst = os.path.join(ASSETS_DIR,f)
            shutil.copy2(src,dst)
def check_files():
    missing = [f for f in REQUIRED_FILES if not os.path.isfile(os.path.join(PROJECT_DIR,f))]
    if missing: return False
    return True
def run_buildozer(mode="debug"):
    cmd = f"buildozer android {mode} deploy run"
    subprocess.call(cmd,shell=True)
def create_output_dir():
    if not os.path.isdir(APK_OUTPUT_DIR):
        os.makedirs(APK_OUTPUT_DIR)
if __name__=="__main__":
    if not check_files():
        exit(1)
    ensure_assets()
    create_output_dir()
    run_buildozer(mode="debug")
    run_buildozer(mode="release")