from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os, requests

titl=input('enter the theme for wallpapers: ')
noOfWallpaper=int(input('enter number of wallpapers required: '))
print('Downloading, please wait')

options = webdriver.FirefoxOptions()
options.headless = True
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe' #Change as per the location of your browser
driverService=Service(r'C:\Users\acer\AppData\Local\Programs\Python\Python39\geckodriver.exe') #location of geckodriver on your device
driver=webdriver.Firefox(service=driverService, options=options)
driver.get('https://wallpapers.com')


os.makedirs(titl+' wallpapers', exist_ok=True) #

searchit=driver.find_elements(By.CLASS_NAME, 'input-group')[0].find_elements(By.ID, 'big-search')
searchit[0].send_keys(titl)
searchit[0].send_keys(Keys.ENTER)


for i in range(1, noOfWallpaper+1):
    print(i)
    xp="/html/body/main/div/div[1]/div[2]/div/div/ul/li["+str(i)+"]/figure/a[1]"
    wurl=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xp)))
    wurl.click()
    time.sleep(1)
    picis=driver.find_elements(By.XPATH, '/html/body/main/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/figure/picture/img')
    walp=picis[0].get_attribute('src')
    

    res=requests.get(walp)
    res.raise_for_status()
    imageFile=open(os.path.join(titl+' wallpapers', os.path.basename(walp)), 'wb')
    for chunk in res.iter_content(1000000):
        imageFile.write(chunk)

    
    searchi=driver.find_elements(By.CLASS_NAME, 'awesomplete')[0].find_elements(By.ID, 'headerSearch')
    searchi[0].send_keys(titl)
    searchi[0].send_keys(Keys.ENTER)

print('Done, Wallpapers downloaded at '+os.path.abspath(titl+' wallpapers'))

          

