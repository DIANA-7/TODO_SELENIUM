import time
from selenium import webdriver
from selenium.webdriver.common.by import By #reconoce el "By" 

driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://demoqa.com/text-box")  # ir y abrir la pagina web
driver.maximize_window()                   # maximizar la pagina
time.sleep(2)                              # esperar 2 segundos

# nombre = driver.find_element(By.ID, "userName")                     # encontrar el campo "nombre" por ID = userName
# nombre = driver.find_element(By.XPATH, "//input[@id='userName']")   # encontrar el campo "nombre" por xpath
# nombre = driver.find_element(By.XPATH, "//*[@id='userName']")       # encontrar el campo "nombre" por xpath 
# nombre = driver.find_element(By.XPATH, "//input[@placeholder='Full Name']")  # encontrar el campo "nombre" por xpath
# nombre.send_keys("Rodrigo")   # enviar la palabra Rodrigo al campo "nombre"

driver.find_element(By.XPATH, "//input[contains(@type,'text')]").send_keys("Rodrigo") # enviar la palabra Rodrigo al campo "nombre"
                 

#driver.implicitly_wait(10) # Espera hasta 10 segundos
#nombre = driver.find_element(By.XPATH, "//input[@id='userName']")

time.sleep(2)
driver.close()


