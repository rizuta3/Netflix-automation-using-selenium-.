from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from credentials import LoginId, password
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()

driver.get('https://netflix.com')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div/a').click()
time.sleep(4)
emailId = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div/div/label/input')
emailId.send_keys(LoginId)
passwordInput = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div['
                                              '2]/div/div/label/input')
passwordInput.send_keys([password])
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/form/button').click()
time.sleep(30)

