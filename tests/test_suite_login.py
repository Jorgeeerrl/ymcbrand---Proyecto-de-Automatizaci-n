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

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testRegistroCorreoErrneo(self):
    self.driver.get("https://www.ymcbrand.com/")
    self.driver.set_window_size(1920, 1080)
    self.driver.find_element(By.LINK_TEXT, "Identificarse").click()
    self.driver.find_element(By.LINK_TEXT, "¿No tienes una cuenta?").click()
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("jorgeeerrloutlook.es")
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Jorge")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("124")
    self.driver.find_element(By.ID, "confirm_password").click()
    self.driver.find_element(By.ID, "confirm_password").send_keys("124")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".alert")
    assert len(elements) > 0
    self.driver.close()
  
  def test_testRegistroUsuarioYaRegistrado(self):
    self.driver.get("https://www.ymcbrand.com/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.LINK_TEXT, "Identificarse").click()
    self.driver.find_element(By.LINK_TEXT, "¿No tienes una cuenta?").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oe_website_login_container").click()
    self.driver.find_element(By.ID, "login").send_keys("jorgeeerrlpruebas@outlook.es")
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Jorgeeerrl")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("124")
    self.driver.find_element(By.ID, "confirm_password").click()
    self.driver.find_element(By.ID, "confirm_password").send_keys("124")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    self.driver.find_element(By.ID, "login").click()
    elements = self.driver.find_elements(By.XPATH, "//p[@class=\'alert alert-danger\'][contains(.,\'Otro usuario ya se ha registrado usando esta dirección de correo electrónico\')]")
    assert len(elements) > 0
    self.driver.close()
  
  def test_testLoginIncorrecto(self):
    self.driver.get("https://www.ymcbrand.com/")
    self.driver.set_window_size(1920, 1080)
    self.driver.find_element(By.LINK_TEXT, "Identificarse").click()
    self.driver.find_element(By.ID, "login").send_keys("jorgeeerrlpruebas@outlook.es")
    self.driver.find_element(By.ID, "password").send_keys("12")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    elements = self.driver.find_elements(By.XPATH, "//p[@class=\'alert alert-danger\'][contains(.,\'Usuario/contraseña incorrecta.\')]")
    assert len(elements) > 0
    self.driver.close()
  
  def test_testLoginCorrecto(self):
    self.driver.get("https://www.ymcbrand.com/")
    self.driver.set_window_size(1920, 1080)
    self.driver.find_element(By.LINK_TEXT, "Identificarse").click()
    self.driver.find_element(By.ID, "login").send_keys("jorgeeerrlpruebas@outlook.es")
    self.driver.find_element(By.ID, "password").send_keys("124")
    self.driver.find_element(By.CSS_SELECTOR, ".oe_website_login_container").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".fw-bold > span").text == "Jorgeeerrl"
    self.driver.close()
  
