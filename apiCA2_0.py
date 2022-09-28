import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome('/content/drive/MyDrive/API_CA/chromedriver.exe')

urlGov = 'http://caepi.mte.gov.br/internet/ConsultaCAInternet.aspx'

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(urlGov)
print(driver)