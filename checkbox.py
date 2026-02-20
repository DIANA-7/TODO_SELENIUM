import time
from selenium import webdriver
from selenium.webdriver.common.by import By #reconoce el "By" 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://demoqa.com/automation-practice-form")  # ir y abrir la pagina web
driver.maximize_window()                   # maximizar la pagina
#time.sleep(2)                              # espera para maximizar ventana
driver.implicitly_wait(2)                   # espera para maximizar ventana



# Set the timeout in seconds (e.g., 10 seconds)
WAIT_TIME = 10

# Define the locator tuple
USER_NAME_LOCATOR = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")

# 1. Wait for the element to be visible and clickable.
#    The .until() method returns the WebElement object.
element = WebDriverWait(driver, WAIT_TIME).until(
    EC.element_to_be_clickable(USER_NAME_LOCATOR)
)

# 2. Perform the action (send_keys) on the returned WebElement object.
element.click()


                 
time.sleep(2)
driver.close()
