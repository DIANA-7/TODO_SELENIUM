import time
from selenium import webdriver
from selenium.webdriver.common.by import By #reconoce el "By" 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://www.exito.com/")  # ir y abrir la pagina web
driver.maximize_window()                   # maximizar la pagina
time.sleep(2)                              # esperar 2 segundos



# obtener el numero de links o elementos con etiqueta <a>  
links = driver.find_elements(By.TAG_NAME,"a")
print("El numero de links que hay en la pagina es: ", len(links))


# obtener el nombre de todos los links o elementos con etiqueta <a> 
for nombres_links in links:
    print(nombres_links.text)


# Encontrar un link y dar clic sobre el link
# DEPRECATED:  driver.find_element_by_link_text ("Súper combos").click()
driver.find_element(By.LINK_TEXT, "Súper combos")
time.sleep(10)    

