import time
from selenium import webdriver
from selenium.webdriver.common.by import By #reconoce el "By" 

driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://demoqa.com/text-box")  # ir y abrir la pagina web
driver.maximize_window()                   # maximizar la pagina
time.sleep(2)                              # esperar 2 segundos


# dar clic en el boton lateral que tiene nombre "Web Tables"
# driver.find_element(By.XPATH, "//span[contains(text(),'Tables')]").click() 

# dar clic en el boton lateral que tiene nombre "Web Tables"
driver.find_element(By.CSS_SELECTOR, "div[class='element-list collapse show'] li[id='item-3'] span[class='text']").click() 

time.sleep(2)
driver.close()