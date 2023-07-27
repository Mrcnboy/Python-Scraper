import requests
from bs4 import BeautifulSoup

from selenium import webdriver
import time

# Instancier le navigateur Chrome
driver = webdriver.Chrome()

# Charger une page Web
driver.get("https://www.google.com")

