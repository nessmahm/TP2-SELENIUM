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

class TestDivision():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_division(self):
    self.driver.get("https://safatelli.github.io/tp-test-logiciel/assets/calc.html")
    self.driver.set_window_size(654, 672)
    self.driver.find_element(By.ID, "num1").click()
    self.driver.find_element(By.ID, "num1").send_keys("10")
    self.driver.find_element(By.ID, "operator").click()
    dropdown = self.driver.find_element(By.ID, "operator")
    dropdown.find_element(By.XPATH, "//option[. = '/']").click()
    self.driver.find_element(By.ID, "num2").click()
    self.driver.find_element(By.ID, "num2").send_keys("0")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
  
