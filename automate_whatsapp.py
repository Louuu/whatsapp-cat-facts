from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests

#Configure Contact Name
contact = ""
number_of_facts = 300
introduction_message = "Hi {0}, I am going to send you {1} cat facts.".format(contact, number_of_facts)

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code and press enter")
input()
print("Logged In")

inp_xpath_search = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]'
input_box_search = WebDriverWait(driver,50).until(lambda  driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)

selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()

inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)

input_box.send_keys(introduction_message + Keys.ENTER)

facts_sent = 0
while facts_sent < number_of_facts:
   print("Sending Fact {0} of {1}".format(facts_sent + 1, number_of_facts))
   fact = requests.get('https://catfact.ninja/fact')
   input_box.send_keys(fact.json()["fact"] + Keys.ENTER)
   facts_sent = facts_sent + 1

print("Mischief Managed!")

time.sleep(5)
driver.quit()