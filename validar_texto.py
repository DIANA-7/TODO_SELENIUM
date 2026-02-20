import time
from selenium import webdriver
from selenium.webdriver.common.by import By #reconoce el "By" 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://demoqa.com/automation-practice-form")  # ir y abrir la pagina web
driver.maximize_window()                   # maximizar la pagina
time.sleep(2)                              # esperar 2 segundos




texto_validado = driver.find_element(By.XPATH, "(//div[contains(@class,'css-1hwfws3')])[2]")
texto_en_etiqueta = texto_validado.text
print("El valor del error es:" + texto_en_etiqueta)

if (texto_en_etiqueta == "Select State"):
    print("falta seleccionar el Estado")

else:
    print("El estado esta seleccionado")


time.sleep(10) 
driver.close()   