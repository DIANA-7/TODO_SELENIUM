import time
from selenium import webdriver
from selenium.webdriver.common.by import By #reconoce el "By" 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://www.demoblaze.com/index.html")  # ir y abrir la pagina web    
driver.maximize_window()                   # maximizar la pagina
#time.sleep(2)                              # espera para maximizar ventana
driver.implicitly_wait(2)                   # espera para maximizar ventana


# Dar clic sobre el boton "about us" que esta en el menu, de esta forma se genera la ventana modal
driver.find_element(By.CSS_SELECTOR, "a[data-target='#videoModal']").click()


# Esperar hasta que se pueda dar clic al boton "Close" y dar clic sobro el boton "Close".
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='videoModal']//button[@type='button'][normalize-space()='Close']"))).click()
time.sleep(10)
