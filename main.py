import time
import pandas as pd
import config as cf
from automation.selenium import GoogleEarthAutomation


timestamp = int(time.time() * 1000)
print(f"Timestamp: {timestamp}")
paths = cf.get_paths(timestamp)
# Example CSV structure: name, data (train/test)
df = pd.read_csv('google_earth_search.csv')
google_earth_bot = GoogleEarthAutomation(timestamp, df)

try:
    google_earth_bot.open_google_earth()
    # google_earth_bot.dismiss_overlay()
    # google_earth_bot.configure_layers()
    # google_earth_bot.process_places()
finally:
    google_earth_bot.close()
