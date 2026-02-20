import time
from selenium import webdriver 

# Ir a sitio web 1:
driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://demoqa.com/automation-practice-form")  # ir y abrir la pagina web
driver.maximize_window()                    # maximizar la pagina
print("ok llegue a pagina demoqa")            
time.sleep(2)                              # esperar 2 segundos


# Ir a sitio web 2:
driver.get("https://www.bvc.com.co/")  # ir y abrir la pagina web
driver.maximize_window()                    # maximizar la pagina
print("ok llegue a la BVC")     
time.sleep(2)                              # esperar 2 segundos


# Ir a sitio web 3:
driver.get("https://maps.google.com/")  # ir y abrir la pagina web
driver.maximize_window()                    # maximizar la pagina
print("ok llegue a google maps")     
time.sleep(2)                              # esperar 2 segundos


# Regresar a sitio web 2:
driver.back()               
print("ok volví a BVC")
time.sleep(2) 

# Regresar a sitio web 1:
driver.back()       
driver.maximize_window()         
print("ok volví a demoqa practice-form")
time.sleep(2) 