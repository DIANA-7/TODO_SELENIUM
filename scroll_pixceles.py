import time
from selenium import webdriver
from selenium.webdriver.common.by import By #reconoce el "By" 

driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://demoqa.com/text-box")  # ir y abrir la pagina web
driver.maximize_window()                   # maximizar la pagina
time.sleep(2)                              # esperar 2 segundos



# Mover barra lateral 500 pixceles hacia abajo (eje y) para visualizar el elemento que vamos a seleccionar
driver.execute_script("window.scroll(0,500)")

# dar clic en el boton lateral que tiene nombre "Dynamic Properties"
driver.find_element(By.CSS_SELECTOR, "div[class='element-list collapse show'] li[id='item-8'] span[class='text']").click() 

time.sleep(10)
driver.close()