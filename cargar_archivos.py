import time
from selenium import webdriver
from selenium.webdriver.common.by import By #reconoce el "By" 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")  # ir y abrir la pagina web    
driver.maximize_window()                   # maximizar la pagina
#time.sleep(2)                              # espera para maximizar ventana
driver.implicitly_wait(2)                   # espera para maximizar ventana


try:

    # buscar el elemento por ID
    buscar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "fileinput"))) 
    buscar = driver.find_element(By.ID, "fileinput")
    
    # carga el archivo docuPruebas240425
    buscar.send_keys("C://TODO_SELENIUM//imagenes//docuPrueba240425.pdf")

    # seleccionar el radio button "A General File"
    driver.find_element(By.XPATH, "//input[@id='itsafile']").click() 

    # dar clic en el boton "Upload"
    driver.find_element(By.XPATH, "//input[@name='upload']").click()
    
    time.sleep(20)


except TimeoutException as ex:   
    print(ex.msg)  
    print("El elemento no esta disponible")