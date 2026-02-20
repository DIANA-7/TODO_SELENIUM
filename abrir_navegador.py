from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
#print(driver.title)
print("ok visita al sitio web y cerrar navegador")
driver.close()