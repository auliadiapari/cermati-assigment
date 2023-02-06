# Manually written script for Selenium WebDriver

from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome();

driver.get('http://cermati.com/app/gabung');

driver.find_element(By.ID, 'email').send_keys('batev74106@bymercy.com')
driver.find_element(by.ID, 'mobilePhone').send_keys('081211806728')
driver.find_element(By.ID, 'password').send_keys('Cermati123!')
driver.find_element(By.ID, 'confirmPassword').send_keys('Cermati123!')
driver.find_element(By.ID, 'firstName').send_keys('Aulia Rachmat!')
driver.find_element(By.ID, 'lastName').send_keys('Diapari')
driver.find_element(By.ID, 'cityAndProvince').send_keys('KOTA DEPOK')
driver.find_element(By.ID, 'terms-and-condition').click()
driver.find_element(By.CSS_SELECTOR, ".RegistrationForm_form-container__button-text__k6N8W").click()

# The scripts started from filling all required fields until clicking on the register button box

pdb.set_trace()


