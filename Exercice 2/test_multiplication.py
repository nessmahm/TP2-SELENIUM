# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestMultiplication():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_multiplication(self):
    self.driver.get("https://safatelli.github.io/tp-test-logiciel/assets/calc.html")
    self.driver.set_window_size(654, 672)
    self.driver.find_element(By.ID, "num1").click()
    self.driver.find_element(By.ID, "num1").send_keys("2")
    self.driver.find_element(By.ID, "operator").click()
    dropdown = self.driver.find_element(By.ID, "operator")
    dropdown.find_element(By.XPATH, "//option[. = '*']").click()
    self.driver.find_element(By.ID, "num2").click()
    self.driver.find_element(By.ID, "num2").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.ID, "result")))
    self.driver.find_element(By.ID, "result").click()
    self.driver.close()
  
