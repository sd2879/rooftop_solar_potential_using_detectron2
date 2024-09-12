import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pyvirtualdisplay import Display
from time import sleep
from config import get_paths

class GoogleEarthAutomation:
    def __init__(self, timestamp, df):
        # Get file paths from config
        self.paths = get_paths(timestamp)
        self.df = df

        # Selenium setup
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--start-maximized')
        self.chrome_options.add_argument('--window-size=1280,720')
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')

        # Virtual display setup
        self.display = Display(visible=0, size=(1280, 720))
        self.display.start()

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.action_chains = ActionChains(self.driver)

    def open_google_earth(self):
        sleep(2)
        self.driver.get("https://earth.google.com/")
        self.driver.set_window_size(1280, 720)
        sleep(5)
        self.driver.save_screenshot(os.path.join(self.paths['run_screenshot'], '1_load_page.png'))
        sleep(2)
    
    def dismiss_overlay(self):
        self.driver.find_element(By.XPATH, "//*").send_keys(Keys.ESCAPE)
        sleep(2)
        self.driver.save_screenshot(os.path.join(self.paths['run_screenshot'], '2_click_esc.png'))
        sleep(2)

    def configure_layers(self):
        self.driver.find_element(By.XPATH, "//*").send_keys(Keys.CONTROL + 'b')
        sleep(5)
        self.driver.save_screenshot(os.path.join(self.paths['run_screenshot'], '3_click_layers.png'))
        sleep(2)
        self.action_chains.move_by_offset(473, 381).click().perform()
        sleep(5)
        self.driver.save_screenshot(os.path.join(self.paths['run_screenshot'], '4_click_layers_clean.png'))
        sleep(2)
        self.action_chains.move_by_offset(-473, -381).perform()
        sleep(2)

    def search_place(self, place):
        self.driver.find_element(By.TAG_NAME, "body").send_keys('/')
        sleep(2)
        self.driver
        self.driver.save_screenshot(os.path.join(self.paths['run_screenshot'], '5_click_search.png'))
        sleep(5)
        # Clear the search field and enter the place name
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + 'a')
        sleep(1)
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.BACKSPACE)
        sleep(1)
        self.driver.find_element(By.TAG_NAME, "body").send_keys(place)
        sleep(1)
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ENTER)
        sleep(10)

    def take_screenshots(self, place, data_type):
        if data_type == 'train':
            self.driver.save_screenshot(os.path.join(self.paths['place_screenshot_marker'], place + ' train_1.png'))
            self.driver.save_screenshot(os.path.join(self.paths['place_screenshot'], place + ' train_1.png'))
        elif data_type == 'test':
            self.driver.save_screenshot(os.path.join(self.paths['place_screenshot_marker'], place + ' test_1.png'))
            self.driver.save_screenshot(os.path.join(self.paths['place_screenshot'], place + ' test_1.png'))

    def process_places(self):
        for x in range(len(self.df)):
            place = self.df['name'][x]
            data_type = self.df['data'][x]
            print(f"Processing {x}: {place}")

            self.search_place(place)
            self.take_screenshots(place, data_type)
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
            sleep(2)

    def close(self):
        self.driver.quit()
        self.display.stop()


