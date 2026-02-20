import time
from selenium import webdriver
from selenium.webdriver.common.by import By #reconoce el "By" 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://demoqa.com/")  # ir y abrir la pagina web
driver.maximize_window()                   # maximizar la pagina
time.sleep(2)                              # esperar 2 segundos

# buscar boton1 por su XPATH
boton1 = driver.find_element(By.XPATH,"//h5[normalize-space()='Elements']")
# imprimir TRUE o FALSE
print(boton1.is_displayed())

# Si es verdad que el boton1 se muestra imprimir "El boton1 existe" de lo contrario imprimir: "El boton1 no existe"
if (boton1.is_displayed() == True):
    print("la imagen del titulo existe") 
    # dar clic en el boton "boton1"
    boton1.click()

else:
    print("No existe la imagen del titulo")

time.sleep(2) 
driver.close()   
