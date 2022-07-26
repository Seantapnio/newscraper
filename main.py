import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
path = "/Users/seant/chromedriver_win32/chromedriver"

# Mandatory Step for SelV.4
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

headers = []
subtitles = []
links = []


for container in containers:
    header = container.find_element(by="xpath", value='./a/h2').text
    subtitle = container.find_element(by="xpath", value='./a/p').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    headers.append(header)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'headers': headers, 'subtitles': subtitles, 'links': links }

pd.DataFrame()




