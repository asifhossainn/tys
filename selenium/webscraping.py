from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# pip install selenium
# Chrome Driver: https://sites.google.com/a/chromium.org/chromedriver/downloads
# https://sites.google.com/chromium.org/driver/?pli=1

PATH = "/home/sribalaji/Downloads/chromedriver-linux64/chromedriver"
driver = webdriver.Chrome(PATH)

options = Options()
options.add_experimental_option('w3c', False)
options.add_argument("--window-size=1920x1080")

driver.get(executable_path = "https://isribalaji.in/", options = options)
