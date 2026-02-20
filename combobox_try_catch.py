import time
from selenium import webdriver
from selenium.webdriver.common.by import By #reconoce el "By" 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://demoqa.com/select-menu")  # ir y abrir la pagina web    
driver.maximize_window()                   # maximizar la pagina
#time.sleep(2)                              # espera para maximizar ventana
driver.implicitly_wait(2)                   # espera para maximizar ventana


try:
    # Set the timeout in seconds (e.g., 10 seconds)
    WAIT_TIME = 5

    # Define the locator tuple
    USER_NAME_LOCATOR = (By.ID, "oldSelectMenu")

    # 1. Wait for the element to be visible and clickable.
    #    The .until() method returns the WebElement object.
    lista_desplegable = WebDriverWait(driver, WAIT_TIME).until(
        EC.element_to_be_clickable(USER_NAME_LOCATOR)
    )

    # 2. Seleccionar la opcion "Magenta" en la lista desplegable 
    seleccionar_color = Select(lista_desplegable)
    seleccionar_color.select_by_visible_text("Magenta")

    print("OK seleccionado el color Magenta")

finally:            
    time.sleep(5)
    driver.quit() # la funcion quit cierra todas las ventanas que esten abiertas, mientras la funion close() cierra una sola ventana.