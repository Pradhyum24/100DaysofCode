import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

response = requests.get("http://appbrewery.github.io/Zillow-Clone/")

soup = BeautifulSoup(response.text,"html.parser")

tags = soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")

prices = []

for tag in tags:
    text = tag.text.strip().replace("/mo", "")  # Remove '/mo'
    parts = text.split("+")
    prices.append(parts[0].strip())

tags = soup.find_all(name="a",class_="StyledPropertyCardDataArea-anchor")
links = []

for tag in tags:
    links.append(tag['href'])

tags = soup.find_all(name="address")
addresses = []

for tag in tags:
    normalized_text = " ".join(tag.text.split())
    addresses.append(normalized_text.replace("|",""))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("link for google sheets")






for i in range(len(prices)):
    time.sleep(2)
    address_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    address_input.send_keys(addresses[i])

    price_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(prices[i])

    link_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(links[i])

    button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    button.click()
    time.sleep(1)

    submit_another = driver.find_element(By.LINK_TEXT, value="Submit another response")
    submit_another.click()

