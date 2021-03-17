#!/usr/bin/env python
import selenium, time, os, platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
import info 

username = info.username
pw = info.password
testing_centers = ['808 Gallery-808 Comm Ave','Agganis Lobby-925 Comm Ave','BUMC-72 E Concord St','Kilachand-610 Comm Ave']

if username =="":
    username = input("Enter your BU username:")
if pw =="":
    pw = getpass("Enter your password:")

if info.choice not in [0,1,2,3]:
    x = int(input("Choose your testing center by typing the corresponding number:  \n 0 = 808 Gallery-808 Comm Ave \n 1 = Agganis Lobby-925 Comm Ave \n 2 = BUMC-72 E Concord St  \n 3 = Kilachand-610 Comm Ave \n "))
    center_select = testing_centers[x]
else:
    center_select = testing_centers[info.choice]

print('Searching for appointments @:', center_select)
#check operating system (windows or mac)
osys = platform.system()

#choose correct chromedriver 
if osys == 'Windows':
    web = webdriver.Chrome('chromedriver.exe')
    
elif osys == 'Darwin':
    web = webdriver.Chrome('chromedriver')


start = time.time()

web.get('https://www.bu.edu/shs/getting-started/using-patient-connect/')
wait = WebDriverWait(web,10)

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-7513"]/p[2]/a'))).click()

#switch tabs 
web.switch_to.window(web.window_handles[1])

#Log in Screen
username_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="j_username"]')))
username_input.send_keys(username)

pw_input = web.find_element_by_xpath('//*[@id="j_password"]')
pw_input.send_keys(pw)

login_button = web.find_element_by_xpath('/html/body/div[1]/div/form/button')
login_button.click()

print("Logging in...")

app_button = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Appointments'))
        )
app_button.click()

wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="cmdSchedule"]'))
    ).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="297"]'))
    ).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="cmdProceed"]'))
    ).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="496"]'))
    ).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="cmdProceed"]'))
    ).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="493"]'))
    ).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="cmdProceed"]'))
    ).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="484"]'))
    ).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="cmdProceed"]'))
    ).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="478"]'))
    ).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="cmdProceed"]'))
    ).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="498"]'))
    ).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="cmdProceed"]'))
    ).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="cmdStandardProceed"]'))
    ).click()

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='LocationList']/option[text() ='"+center_select+"']"))
    ).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="apptSearch"]'))
    ).click()


#Wait for Success Page
wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/h1')))
title = web.find_element_by_xpath('/html/body/div[2]/div/div[2]/h1')
while title.text != "All Done!":
    time.sleep(1)
web.quit()
