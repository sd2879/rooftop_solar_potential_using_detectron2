import os
import subprocess
from time import sleep
import sys

def install_packages():
    """Install Python packages from requirements.txt."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def install_system_packages():
    """Install system packages required for Selenium and virtual display."""
    subprocess.check_call(["apt-get", "update"])
    subprocess.check_call(["apt-get", "install", "-y", "xvfb"])
    subprocess.check_call(["pip", "install", "pyvirtualdisplay", "selenium"])

def setup_virtual_display():
    """Set up a virtual display using pyvirtualdisplay."""
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(1280, 720))
    display.start()
    sleep(5)
    display.stop()

def clone_repository():
    """Clone the GitHub repository if it doesn't already exist."""
    repo_dir = 'rooftop_solar_potential_using_detectron2'
    if not os.path.exists(repo_dir):
        subprocess.check_call(["git", "clone", "https://github.com/sd2879/rooftop_solar_potential_using_detectron2.git"])

def main():
    """Main function to set up the environment and run the setup."""
    clone_repository()
    os.chdir('rooftop_solar_potential_using_detectron2')
    # install_packages()
    install_system_packages()
    setup_virtual_display()
    # Optionally, run the script here
    # subprocess.check_call(["python", "main.py"])

if __name__ == "__main__":
    main()
