import os
import subprocess
import sys

def install_packages():
    # Install Python packages from requirements.txt
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def install_system_packages():
    # Install system packages required for Selenium
    subprocess.check_call(["apt-get", "update"])
    subprocess.check_call(["apt-get", "install", "-y", "wget", "unzip"])
    subprocess.check_call(["wget", "https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip"])
    subprocess.check_call(["unzip", "chromedriver_linux64.zip"])
    subprocess.check_call(["mv", "chromedriver", "/usr/local/bin/"])
    subprocess.check_call(["apt-get", "install", "-y", "chromium-browser"])

def setup_virtual_display():
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(1280, 720))
    display.start()

def clone_repository():
    # Clone the GitHub repository
    if not os.path.exists('your_repository'):
        subprocess.check_call(["git", "clone", "https://github.com/sd2879/rooftop_solar_potential_using_detectron2.git"])

def main():
    clone_repository()
    os.chdir('your_repository')
    install_packages()
    install_system_packages()
    setup_virtual_display()
    # Optionally, run the script here
    # subprocess.check_call(["python", "main.py"])

if __name__ == "__main__":
    main()
