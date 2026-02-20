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

# buscar el titulo por su XPATH
titulo = driver.find_element(By.XPATH,"//img[@src='/images/Toolsqa.jpg']")
# imprimir TRUE o FALSE
print(titulo.is_displayed())
# buscar el boton "Elements"
boton_elements = driver.find_element(By.XPATH, "//h5[normalize-space()='Elements']")

# Si es verdad que el titulo se muestra imprimir "la imagen del titulo existe" de lo contrario imprimir: "No existe la imagen del titulo"
if (titulo.is_displayed() == True):
    print("la imagen del titulo existe") 
    # dar clic en el boton "elements"
    boton_elements.click()

else:
    print("No existe la imagen del titulo")

time.sleep(2) 
driver.close()   
