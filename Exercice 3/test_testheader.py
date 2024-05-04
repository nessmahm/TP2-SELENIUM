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

class TestTestheader():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testheader(self):
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(1296, 688)
    self.driver.find_element(By.LINK_TEXT, "Contact").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, "#exampleModal .modal-header")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "recipient-email").click()
    self.driver.find_element(By.ID, "recipient-email").send_keys("user")
    self.driver.find_element(By.ID, "recipient-name").send_keys("name")
    self.driver.find_element(By.ID, "message-text").click()
    self.driver.find_element(By.ID, "message-text").send_keys("message")
    self.driver.find_element(By.CSS_SELECTOR, "#exampleModal .btn-primary").click()
    assert self.driver.switch_to.alert.text == "Thanks for the message!!"
  