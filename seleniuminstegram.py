from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from time import sleep 
username = input("Your Username") 
password = input("Your Password") 
driver = webdriver.Edge(executable_path="E:\\msedgedriver.exe")

driver.get("https://www.instagram.com/") 
sleep(4)
sendusercontent = driver.find_element(By.NAME,"username")  
sendusercontent.send_keys(username) 
sendpasswordcontent = driver.find_element(By.NAME,"password") 
sendpasswordcontent.send_keys(password) 
sendpasswordcontent.send_keys(Keys.ENTER) 
sleep(5) 
if (driver.find_element(By.CLASS_NAME,"cmbtv")): 
      
 driver.find_element(By.CLASS_NAME,"cmbtv").find_element(By.TAG_NAME,"button").click()
sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click() 
driver.get("https://www.instagram.com/res.osman/") 
 
sleep(7)
follow = driver.find_element(By.CSS_SELECTOR,"._acan._acap._acas").click()  
import os 





 


