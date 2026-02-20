import time
from selenium import webdriver
from selenium.webdriver.common.by import By #reconoce el "By" 

driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://demoqa.com/text-box")  # ir y abrir la pagina web
driver.maximize_window()                   # maximizar la pagina
time.sleep(2)                              # esperar 2 segundos



driver.find_element(By.XPATH, "//input[@type='text' and @id='userName']").send_keys("Rodrigo") # enviar la palabra Rodrigo al campo "nombre"
                 

time.sleep(2)
driver.close()